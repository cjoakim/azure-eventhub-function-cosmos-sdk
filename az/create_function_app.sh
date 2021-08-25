#!/bin/bash

source ../config.sh

# Note: I executed this commands one at a time

# az login
# az account set --subscription $AZURE_SUBSCRIPTION_ID
# az account show
# az group create --name $rg --location $region

# az storage account create \
#     --name $storage_name \
#     --location $region \
#     --resource-group $rg \
#     --sku Standard_LRS

# az functionapp create \
#     --resource-group $rg \
#     --consumption-plan-location $region \
#     --runtime dotnet \
#     --functions-version 3 \
#     --name $function_app_name \
#     --storage-account $storage_name

# warning message:
# --runtime-version is not supported for --runtime dotnet.
# Dotnet version is determined by --functions-version.
# Dotnet version will be 3.1 for this function app.
