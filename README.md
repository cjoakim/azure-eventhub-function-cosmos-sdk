# azure-eventhub-function-cosmos-sdk

azure-eventhub-function-cosmos-sdk

## Links

- https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-function-linux-custom-image?tabs=in-process%2Cbash%2Cazure-cli&pivots=programming-language-csharp
- https://docs.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide


## Function App


```
#!/bin/bash
#docker build --tag <DOCKER_ID>/azurefunctionsimage:v1.0.0 .
docker build -t cjoakim/azure-eventhub-function-cosmos-sdk .




$ func --version
3.0.3568

$ mkdir function_app
$ cd function_app/

$ func init App1 --dotnet

$ cd App1

$ func new --name HttpToEvtHub --template "HTTP trigger" --authlevel "anonymous"

The function "HttpToEvtHub" was created successfully from the "HTTP trigger" template.


$ dotnet build
Build succeeded

$ func start

Functions:
	HttpToEvtHub: [GET,POST] http://localhost:7071/api/HttpToEvtHub

$ curl http://localhost:7071/api/HttpToEvtHub?name=elsa
Hello, elsa. This HTTP triggered function executed successfully.




```