#!/bin/bash

source ../../config.sh

echo 'publishing functionapp: '$function_app_name

func azure functionapp publish $function_app_name



# $ ./publish.sh
# Microsoft (R) Build Engine version 16.9.0+57a23d249 for .NET
# Copyright (C) Microsoft Corporation. All rights reserved.

#   Determining projects to restore...
#   All projects are up-to-date for restore.
#   App1 -> /Users/cjoakim/github/azure-eventhub-function-cosmos-sdk/function_app/App1/bin/publish/App1.dll

# Build succeeded.
#     0 Warning(s)
#     0 Error(s)

# Time Elapsed 00:00:02.16


# Getting site publishing info...
# Creating archive for current directory...
# Uploading 2.3 MB [################################################################################]
# Upload completed successfully.
# Deployment completed successfully.
# Syncing triggers...
# Functions in cjoakimfunctions1:
#     HttpToEvtHub - [httpTrigger]
#         Invoke url: https://cjoakimfunctions1.azurewebsites.net/api/httptoevthub