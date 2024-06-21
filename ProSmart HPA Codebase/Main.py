#*********************************************************** This file runs the Microservice Managers in parallel ***********************************************************************

import time
import os
import subprocess
import multiprocessing
from multiprocessing import Pool
from functools import partial
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



def run_function(func):
    return func()


# ********************************************************************** Starting the ProSmart HPA operation ************************************************************************
#   Initializing Test Time

desired_time = 900     # Total_Test_Time = 900sec = 15 minutes 
start_time = time.time()

if __name__ == '__main__':

    while (time.time() - start_time) < desired_time:

        Test_Time = time.time() - start_time

        # ********************************************************************** Running Microservice Managers in Parallel  **********************************************

        functions = [partial(frontend, Test_Time), partial(adservice, Test_Time), partial(cartservice, Test_Time), partial(currencyservice, Test_Time), partial(checkoutservice, Test_Time), partial(emailservice, Test_Time), partial(paymentservice, Test_Time), partial(shippingservice, Test_Time), partial(productcatalogservice, Test_Time), partial(recommendationservice, Test_Time), partial(redis, Test_Time)]
        with multiprocessing.Pool(processes=len(functions)) as pool:
            pool.map(run_function, functions)              # Running the microservice managers functions in parallel

            for _ in pool:            # Wait for each microservice process to finish to start next iteration
                _.join()
      
        
