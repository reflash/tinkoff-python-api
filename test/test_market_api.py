# coding: utf-8

"""
    OpenAPI

    tinkoff.ru/invest OpenAPI.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: n.v.melnikov@tinkoff.ru
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import tinkoff_api_client
from api.market_api import MarketApi  # noqa: E501
from tinkoff_api_client.rest import ApiException


class TestMarketApi(unittest.TestCase):
    """MarketApi unit test stubs"""

    def setUp(self):
        self.api = api.market_api.MarketApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_market_bonds_get(self):
        """Test case for market_bonds_get

        Получение списка облигаций  # noqa: E501
        """
        pass

    def test_market_currencies_get(self):
        """Test case for market_currencies_get

        Получение списка валютных пар  # noqa: E501
        """
        pass

    def test_market_etfs_get(self):
        """Test case for market_etfs_get

        Получение списка ETF  # noqa: E501
        """
        pass

    def test_market_search_by_figi_get(self):
        """Test case for market_search_by_figi_get

        Получение инструмента по FIGI  # noqa: E501
        """
        pass

    def test_market_search_by_ticker_get(self):
        """Test case for market_search_by_ticker_get

        Получение инструмента по тикеру  # noqa: E501
        """
        pass

    def test_market_stocks_get(self):
        """Test case for market_stocks_get

        Получение списка акций  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
