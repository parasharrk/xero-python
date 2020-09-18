# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.3.0
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Balances(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "accounts_receivable": "AccountsReceivable",
        "accounts_payable": "AccountsPayable",
    }

    attribute_map = {
        "accounts_receivable": "AccountsReceivable",
        "accounts_payable": "AccountsPayable",
    }

    def __init__(self, accounts_receivable=None, accounts_payable=None):  # noqa: E501
        """Balances - a model defined in OpenAPI"""  # noqa: E501

        self._accounts_receivable = None
        self._accounts_payable = None
        self.discriminator = None

        if accounts_receivable is not None:
            self.accounts_receivable = accounts_receivable
        if accounts_payable is not None:
            self.accounts_payable = accounts_payable

    @property
    def accounts_receivable(self):
        """Gets the accounts_receivable of this Balances.  # noqa: E501


        :return: The accounts_receivable of this Balances.  # noqa: E501
        :rtype: AccountsReceivable
        """
        return self._accounts_receivable

    @accounts_receivable.setter
    def accounts_receivable(self, accounts_receivable):
        """Sets the accounts_receivable of this Balances.


        :param accounts_receivable: The accounts_receivable of this Balances.  # noqa: E501
        :type: AccountsReceivable
        """

        self._accounts_receivable = accounts_receivable

    @property
    def accounts_payable(self):
        """Gets the accounts_payable of this Balances.  # noqa: E501


        :return: The accounts_payable of this Balances.  # noqa: E501
        :rtype: AccountsPayable
        """
        return self._accounts_payable

    @accounts_payable.setter
    def accounts_payable(self, accounts_payable):
        """Sets the accounts_payable of this Balances.


        :param accounts_payable: The accounts_payable of this Balances.  # noqa: E501
        :type: AccountsPayable
        """

        self._accounts_payable = accounts_payable
