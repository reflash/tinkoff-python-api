# swagger_client.OrdersApi

All URIs are relative to *https://api-invest.tinkoff.ru/openapi/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orders_cancel_post**](OrdersApi.md#orders_cancel_post) | **POST** /orders/cancel | Отмена заявки
[**orders_get**](OrdersApi.md#orders_get) | **GET** /orders | Получение списка активных заявок
[**orders_limit_order_post**](OrdersApi.md#orders_limit_order_post) | **POST** /orders/limit-order | Создание лимитной заявки

# **orders_cancel_post**
> Empty orders_cancel_post(order_id, body=body)

Отмена заявки

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
order_id = 'order_id_example' # str | ID заявки
body = swagger_client.Empty() # Empty |  (optional)

try:
    # Отмена заявки
    api_response = api_instance.orders_cancel_post(order_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_cancel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID заявки | 
 **body** | [**Empty**](Empty.md)|  | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_get**
> OrdersResponse orders_get()

Получение списка активных заявок

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))

try:
    # Получение списка активных заявок
    api_response = api_instance.orders_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrdersResponse**](OrdersResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_limit_order_post**
> LimitOrderResponse orders_limit_order_post(body, figi)

Создание лимитной заявки

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
body = swagger_client.LimitOrderRequest() # LimitOrderRequest | 
figi = 'figi_example' # str | FIGI инструмента

try:
    # Создание лимитной заявки
    api_response = api_instance.orders_limit_order_post(body, figi)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_limit_order_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LimitOrderRequest**](LimitOrderRequest.md)|  | 
 **figi** | **str**| FIGI инструмента | 

### Return type

[**LimitOrderResponse**](LimitOrderResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

