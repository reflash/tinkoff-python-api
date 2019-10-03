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

import swagger_client
from api.sandbox_api import SandboxApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSandboxApi(unittest.TestCase):
    """SandboxApi unit test stubs"""

    def setUp(self):
        self.api = api.sandbox_api.SandboxApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sandbox_clear_post(self):
        """Test case for sandbox_clear_post

        Удаление всех позиций  # noqa: E501
        """
        pass

    def test_sandbox_currencies_balance_post(self):
        """Test case for sandbox_currencies_balance_post

        Выставление баланса по валютным позициям  # noqa: E501
        """
        pass

    def test_sandbox_positions_balance_post(self):
        """Test case for sandbox_positions_balance_post

        Выставление баланса по инструментным позициям  # noqa: E501
        """
        pass

    def test_sandbox_register_post(self):
        """Test case for sandbox_register_post

        Регистрация клиента в sandbox  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()