# swagger_client.PortfolioApi

All URIs are relative to *https://api-invest.tinkoff.ru/openapi/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**portfolio_currencies_get**](PortfolioApi.md#portfolio_currencies_get) | **GET** /portfolio/currencies | Получение валютных активов клиента
[**portfolio_get**](PortfolioApi.md#portfolio_get) | **GET** /portfolio | Получение портфеля клиента

# **portfolio_currencies_get**
> PortfolioCurrenciesResponse portfolio_currencies_get()

Получение валютных активов клиента

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PortfolioApi(swagger_client.ApiClient(configuration))

try:
    # Получение валютных активов клиента
    api_response = api_instance.portfolio_currencies_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->portfolio_currencies_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PortfolioCurrenciesResponse**](PortfolioCurrenciesResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portfolio_get**
> PortfolioResponse portfolio_get()

Получение портфеля клиента

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PortfolioApi(swagger_client.ApiClient(configuration))

try:
    # Получение портфеля клиента
    api_response = api_instance.portfolio_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->portfolio_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PortfolioResponse**](PortfolioResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

