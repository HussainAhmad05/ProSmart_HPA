## ProSmart HPA: A Proactive and Resource-Efficient Horizontal Pod Auto-scaler for Microservice Architectures

This repository includes the codebase and implementation specifics of the intelligent hierarchical MAPE-KI architecture of ProSmart HPA, along with its local and global scaling policies.

### Table of Contents

The package contains the following directories.

#### 1. Benchmark Application
This folder comprises the source and deployment files for each microservice within the microservice benchmark application, as well as the load test script. Further details regarding the benchmark application can be found at https://github.com/GoogleCloudPlatform/microservices-demo.

#### 2. ProSmartHPA Codebase
This folder contains the Microservice Managers alongside their corresponding trained PROPHET models to predict microservice resource demand, each dedicated to a specific microservice within the benchmark application. Additionally, the Application Resource Manager and trained PROPHET models to predict resource capacities for microservices are also included as part of the codebase.

#### 3. Results Analysis
The script utilized to determine and analyze the evaluation metrics from the recorded data, evaluating the performance of ProSmart HPA, can be found in this folder. 

#### 4. Results Visualization
The folder contains the script that is used for data visualization and generating the bar graphs for both Figure 4 and Figure 5 as presented in the paper.








## Initial Configurations

To set up and operate ProSmart HPA, you will require an AWS EKS cluster and 10 AWS EC2 instances for running the microservice benchmark application. Additionally, you will need a separate machine to run ProSmart HPA and the load testing tool, Locust (https://locust.io). The configurations required for AWS EKS cluster, EC2 instances and local machine are as follows:

#### EKS Cluster Configurations

The Amazon EKS cluster employs Kubernetes version 1.24, with default AWS VPC network and subnet settings, IPv4 IP cluster family, API server endpoints having both private and public network access, and incorporates add-ons networking features of EKS cluster, such as kube-proxy, CoreDNS, and VPC CNI.

#### EC2 instances configurations

Each EC2 instance (VM machine) is configured as a t3.medium instance, equipped with an Intel Xeon Platinum 8000 series processor,  2-core 3.1 GHz CPU, 4GB of RAM, 5Gbps network bandwidth, 5GiB disk size, supporting up to 3 elastic network interfaces and 18 IP addresses. All 10 EC2 instances run on the Linux operating system (AL2_x86_64) with the EKS-optimized Amazon Linux AMI.

#### Local Machine Configurations

ProSmart HPA and Load Generating Tool (i.e., Locust) are hosted on a local machine, featuring an Intel Corei7 2.60GHz CPU and 16GB RAM. ProSmart HPA is connected to the application running on AWS EKS through the AWS command-line interface.

#### Setting up the Python Environment

To begin, ensure that you have installed all the dependencies specified at the beginning of the "Main", "Microservice Managers", and "Application Resource Manager" scripts. Additionally, place the knowledge base, trained PROPHET models, Application Resource Manager, and all other Microservice Manager scripts in the same directory as the "Main" script. Alternatively, you can edit the directory paths within the scripts to match your specific directory structure.








# Setup Steps for ProSmart HPA

#### Step 1: Connect EKS Cluster with Local Machine
Create an EKS Cluster on AWS account with 10 EC2 nodes (VM machines) with the specified configurations. Connect the EKS cluster with the local machine through the following command.

```sh
   aws eks update-kubeconfig --region YourRegionName --name YourClusterName
```


#### Step 2: Deploy the Benchmark Application
Deploy the benchmark application (Online Boutique) to the EKS cluster:

```sh
kubectl apply -f ./release/kubernetes-manifests.yaml
```
You can find more details at https://github.com/GoogleCloudPlatform/microservices-demo 

#### Step 3: Install metrics server on AWS EKS cluster

Installation instructions can be found at https://docs.aws.amazon.com/eks/latest/userguide/metrics-server.html 

Verify the installation: 

```sh
kubectl top pod
```

#### Step 4: Get the Frontend's External IP (Benchmark Application Access Link)

```sh
kubectl get all
```

Note the frontend’s external IP, for example: a4aa7c15864d64938addf2e4f76e84ef-313638180.xxxxxxxxx.amazonaws.com

Access the web frontend in a browser using the frontend's external IP.

#### You have now successfully set up the benchmark application, EKS cluster, and EC2 worker nodes.

### Step 5 and 6 Run in Parallel

These steps should be run in parallel, starting at the same time.

#### Step 5: Run ProSmart HPA

Run the “Main” script placed in the ProSmart HPA Codebase folder. It will call the Microservice Managers scripts and the Microservice Managers call the Application Resource Manager script in resource-constrained environments. Ensure these scripts are placed in the same directory as Main Script (otherwise, you may change these directories, and edit the corresponding scripts accordingly). Verify the path of the Knowledge Base in the scripts of Microservice Managers as per your settings.

#### Step 6: Run Load Test Script

Run the Load Test Script placed in the benchmark application. Go to the directory of the Load Test script in the command window and enter the following command:

```sh
locust -f Load_Test_Script.py --host=YourFrontendIP --csv=my_results --csv-full-history
```

Open the browser and go to the Locust interface through http://localhost:8089 to run the load test.

Configure the load test settings:

Number of Users: 600, 
Spawn Rate: 2, 
Host: Your frontend’s external IP address, 
Time: 900s (i.e., 15 minutes)
