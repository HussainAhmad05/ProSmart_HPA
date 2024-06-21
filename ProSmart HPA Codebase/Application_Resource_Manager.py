#***************************************************** This file outlines the algorithm for Microservice Manager responsible for the frontend microservice **********************************************

import sys
import fnmatch
import glob, os
import subprocess
import math
import numpy as np
import time
import statistics
from openpyxl import Workbook, load_workbook
import pandas as pd
import pickle
from frontend import *
from adservice import *
from cartservice import *
from checkoutservice import *
from currencyservice import *
from emailservice import *
from paymentservice import *
from productcatalogservice import *
from recommendationservice import *
from shippingservice import *
from rediscart import *


#************************************************************************************ Monitor Component **********************************************************************************************

def Monitor (microservice_name):                                                              # Getting essential data from the microservices


    with open(f'{microservice_name}.txt', 'r') as file:

        lines = file.readlines()  # Read all metrics from the file of that microservice

        Predicted_Demand = int(lines[0].strip())
        scaling_action = lines[1].strip()
        current_replicas = int(lines[2].strip())
        max_replica = int(lines[3].strip())
        cpu_request = int(lines[4].strip())


    return Predicted_Demand, scaling_action, current_replicas, max_replica, cpu_request  



#***************************************************************************** Analyze Component *****************************************************************************************


def Analyse (Predicted_Time, microservice_name, Predicted_Demand, max_replica, current_replicas):

    with open(microservice_name+'_capacity_model.pkl', 'rb') as f:                          #Loading of trained PROPHET model for predicting microservice resource capacity
            globals()[microservice_name+'_model']  = pickle.load(f)

    
    future = pd.DataFrame({'ds': [Predicted_Time]})

    # Add real-time regressor values to the future dataframe 
    
    futures  = future.copy() 
    futures.index = pd.to_datetime(futures.ds)   
    regressors = pd.concat([max_replica, current_replicas, Predicted_Demand], axis=1)    
    futures = futures.merge(regressors, left_index=True, right_index=True)     
    futures = futures.reset_index(drop = True)
    
    # Make prediction

    forecast            = globals()[microservice_name+'_model'].predict(future)
    Predicted_Capacity  = math.ceil(forecast ['yhat'])   

    return Predicted_Capacity

#***************************************************************************** Plan Component *****************************************************************************************

def Plan(Predicted_Demand_array, Predicted_Capacity_array, max_replica_array, cpu_request_array):

    added_resource, removed_resource = 0, 0

    for i in range(11):
          
        if (Predicted_Capacity_array[i] > max_replica_array[i]):                            # predicted capacity > original capacity
            added_resource = added_resource + (( Predicted_Capacity_array[i] - max_replica_array[i] ) * cpu_request_array[i])
        else:
            removed_resource = removed_resource + (( max_replica_array[i] - Predicted_Capacity_array[i] ) * cpu_request_array[i])

    # Determining overprovisioned and underprovisioned microservices

    over = np.argsort((Predicted_Capacity_array - Predicted_Demand_array) * cpu_request_array) # sorted fom Most overprovisioned to least overprovisioned microservice
    under = np.argsort((Predicted_Demand_array - Predicted_Capacity_array) * cpu_request_array) # sorted fom Most underprovisioned to least underprovisioned microservice
    
    # Balancing added and removed resource by PROPHET (if added_resource != removed_resource)

    while (added_resource != removed_resource):
        if (added_resource > removed_resource):
            resource_needs_to_be_removed = added_resource - removed_resource
            j = 0                                           # most to least overprovisioned microservices index
            while (resource_needs_to_be_removed != 0):
                Overprovisioned_resource = ((Predicted_Capacity_array[over[j]] - Predicted_Demand_array[over[j]]) * cpu_request_array[over[j]])                 
                if (resource_needs_to_be_removed > Overprovisioned_resource):
                    removed_resource = removed_resource + Overprovisioned_resource
                    Predicted_Capacity_array[over[j]] = Predicted_Demand_array[over[j]]
                else:
                    Remaining_resource = Overprovisioned_resource - resource_needs_to_be_removed
                    Predicted_Capacity_array[over[j]] = Predicted_Demand_array[over[j]] + math.floor(Remaining_resource/cpu_request_array[over[j]])
                    removed_resource = removed_resource + resource_needs_to_be_removed
                j = j+1
                resource_needs_to_be_removed = added_resource - removed_resource
        else:
            resource_needs_to_be_added = removed_resource - added_resource
            j = 0
            while (resource_needs_to_be_added != 0):
                # if (residual_capacity > diff):
                Underprovisioned_resource = ((Predicted_Demand_array[under[j]] - Predicted_Capacity_array[under[j]]) * cpu_request_array[under[j]])
                if (resource_needs_to_be_added > Underprovisioned_resource):
                    Predicted_Capacity_array[under[j]] = Predicted_Capacity_array[under[j]] + math.floor(Underprovisioned_resource/cpu_request_array[under[j]])
                    added_resource = added_resource + Underprovisioned_resource
                else:
                    Predicted_Capacity_array[under[j]] = Predicted_Capacity_array[under[j]] + math.floor(resource_needs_to_be_added/cpu_request_array[under[j]])
                    added_resource = added_resource + resource_needs_to_be_added
                j = j+1
                resource_needs_to_be_added =  removed_resource - added_resource              
         
    return Predicted_Capacity_array

#***************************************************************************** Execute Component *****************************************************************************************

def Execute (Predicted_Demand_array, Predicted_Capacity_array, scaling_action_array, current_replicas_array):

    resource_wise_SD_array = np.zeros(11)
    resource_wise_DR_array = np.zeros(11)

    for i in range(11):
        if (Predicted_Capacity_array[i] >= Predicted_Demand_array[i]):

            resource_wise_SD_array[i] = scaling_action_array[i]
            resource_wise_DR_array[i] = Predicted_Demand_array[i]

        elif (Predicted_Capacity_array[i] > current_replicas_array[i]) and (Predicted_Capacity_array[i] < Predicted_Demand_array[i]):

            resource_wise_SD_array[i] = "scale up"
            resource_wise_DR_array[i] = Predicted_Capacity_array[i]
        else:
            resource_wise_SD_array[i] = "no scale"
            resource_wise_DR_array[i] = current_replicas_array[i]

    return resource_wise_SD_array, resource_wise_DR_array



#***************************************************************************** Main Function of Application Resource Manager *****************************************************************************************


def Application_Resource_Manager(Predicted_Time):

    ARM_status = 1                      # ARM status represents the status of the Application Resource Manager; 1 presents the activation of the Application Resource Manager

    # Initializing arrays of length 11 for storing metrics of all 11 microservices
    Predicted_Demand_array = np.zeros(11)
    scaling_action_array = np.zeros(11)
    current_replicas_array = np.zeros(11)
    max_replica_array = np.zeros(11)
    cpu_request_array = np.zeros(11)
    Predicted_Capacity_array = np.zeros(11)

    microservice_name = ["frontend", "adservice", "cartservice", "paymentservice", "currencyservice", "emailservice", "checkoutservice", "productcatalogueservice", "recommendationservice", "redis-cart", "shippingservice"]

    # When Application_Resource_Manager is triggered by any microservice, it will get the essential metrics from all microservices through its Monitor component

    for i in range(11):
        Predicted_Demand_array[i], scaling_action_array[i], current_replicas_array[i], max_replica_array[i], cpu_request_array[i]  = Monitor(microservice_name[i])

    # Analyze component predicts the resource capacities for all 11 microservices

    for i in range(11):    
        Predicted_Capacity_array[i] = Analyse (Predicted_Time, microservice_name[i], Predicted_Demand_array[i], max_replica_array[i], current_replicas_array[i])

    # Plan component ensures that the resources added and removed by PROPHET are balanced. If they're not equal, it reallocates resources among microservices to achieve parity

    Predicted_Capacity_array = Plan(Predicted_Demand_array, Predicted_Capacity_array, max_replica_array, cpu_request_array)

    # Execute component determines resource-wise scaling actions, and resource demands as per the predicted resource capacities of microservices

    resource_wise_SD_array, resource_wise_DR_array = Execute (Predicted_Demand_array, Predicted_Capacity_array, scaling_action_array, current_replicas_array)

    
    # Storing the resource-efficient results for each microservice in a separate file so that each microservice manager can access its corresponding metrics from its file  

    ARM_microservice_name = ["ARM_frontend", "ARM_adservice", "ARM_cartservice", "ARM_paymentservice", "ARM_currencyservice", "ARM_emailservice", "ARM_checkoutservice", "ARM_productcatalogueservice", "ARM_recommendationservice", "ARM_redis-cart", "ARM_shippingservice"]
    
    i = 0
    for service in ARM_microservice_name:  
        with open(f'{service}.txt', 'w') as file:
            file.write(f'{ARM_status}\n')
            file.write(f'{resource_wise_SD_array[i]}\n')
            file.write(f'{resource_wise_DR_array[i]}\n')
            file.write(f'{Predicted_Capacity_array[i]}\n')
        i = i + 1
    
    
    return



