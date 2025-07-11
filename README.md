# Kidney-Disease-Classification-MLFlow-DVC 


'''
# Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py


'''




# How to run?

### STEPS:

clone the repository

''' bash
https://github.com/Nisargak18/Kidney-Disease-Classification-Deep-Learning-Project
'''

### STEP 01- Create a conda environment after opening the repository

'''bash
conda create -n cnncls python=3.10 -y
'''

'''bash
conda activate cnncls
'''

### STEP 02- install the requirements

'''bash
pip install -r requirments.txt
'''




### MLflow



### cmd
mlflow ui

### dagshub
'''

MLFLOW_TRACKING_URI="https://dagshub.com/Nisargak18/Kidney-Disease-Classification-Deep-Learning-Project.mlflow"
MLFLOW_TRACKING_USERNAME="Nisargak18"
MLFLOW_TRACKING_PASSWORD="mlflow-token"
python script.py

Run this to export as env variables:

export MLFLOW_TRACKING_URI=https://dagshub.com/Nisargak18/Kidney-Disease-Classification-Deep-Learning-Project.mlflow

export MLFLOW_TRACKING_USERNAME=Nisargak18

export MLFLOW_TRACKING_PASSWORD=
'''

### DVC cmd

1.dvc init
2.dvc repro
3.dvc dag 


### About MLflow & DVC
 ## MLflow

Its Production Grade
Trace all of your expriements
Logging & taging your model

## DVC

Its very lite weight for POC only
lite weight expriements tracker
It can perform Orchestration (Creating Pipelines)



### GCP-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2.Prerequisites
A Google Cloud project.

Dockerfile present in your project root.

GitHub repository connected to this project.

Enabled Cloud Run API on GCP.

GitHub Secrets configured:

GCP_PROJECT_ID – your GCP project ID.

GCP_REGION – your deployment region (e.g., us-central1).

GCP_SA_KEY – service account JSON key (as a string)

## 3. Setting Up Secrets
# In Google Cloud Console:

Go to IAM & Admin → Service Accounts.

Create a service account named github-cicd.

Assign the roles:

Cloud Run Admin

Storage Admin

Artifact Registry Writer

Viewer

Generate a JSON key and download it.

## 4.In GitHub repo:

Go to Settings → Secrets → Actions.

Add the following secrets:

GCP_PROJECT_ID

GCP_REGION

GCP_SA_KEY (contents of the JSON key)



### GitHub Actions Workflow
.github/workflows/gcp-deploy.yml


### Final
https://kidney-predictor-100626608651.us-central1.run.app/