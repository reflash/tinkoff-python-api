# tinkoff_api_client.OperationsApi

All URIs are relative to *https://api-invest.tinkoff.ru/openapi/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operations_get**](OperationsApi.md#operations_get) | **GET** /operations | Получение списка операций

# **operations_get**
> OperationsResponse operations_get(_from, interval, figi=figi)

Получение списка операций

### Example
```python
from __future__ import print_function
import time
import tinkoff_api_client
from tinkoff_api_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tinkoff_api_client.OperationsApi(tinkoff_api_client.ApiClient(configuration))
_from = '2013-10-20' # date | Начало временного промежутка
interval = tinkoff_api_client.OperationInterval() # OperationInterval | Длительность временного промежутка
figi = 'figi_example' # str | Figi инструмента для фильтрации (optional)

try:
    # Получение списка операций
    api_response = api_instance.operations_get(_from, interval, figi=figi)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Начало временного промежутка | 
 **interval** | [**OperationInterval**](.md)| Длительность временного промежутка | 
 **figi** | **str**| Figi инструмента для фильтрации | [optional] 

### Return type

[**OperationsResponse**](OperationsResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

