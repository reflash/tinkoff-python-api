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
from api.operations_api import OperationsApi  # noqa: E501
from tinkoff_api_client.rest import ApiException


class TestOperationsApi(unittest.TestCase):
    """OperationsApi unit test stubs"""

    def setUp(self):
        self.api = api.operations_api.OperationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_operations_get(self):
        """Test case for operations_get

        Получение списка операций  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
