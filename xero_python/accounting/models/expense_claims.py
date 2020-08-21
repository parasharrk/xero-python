# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.2.13
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class ExpenseClaims(BaseModel):
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
    openapi_types = {"expense_claims": "list[ExpenseClaim]"}

    attribute_map = {"expense_claims": "ExpenseClaims"}

    def __init__(self, expense_claims=None):  # noqa: E501
        """ExpenseClaims - a model defined in OpenAPI"""  # noqa: E501

        self._expense_claims = None
        self.discriminator = None

        if expense_claims is not None:
            self.expense_claims = expense_claims

    @property
    def expense_claims(self):
        """Gets the expense_claims of this ExpenseClaims.  # noqa: E501


        :return: The expense_claims of this ExpenseClaims.  # noqa: E501
        :rtype: list[ExpenseClaim]
        """
        return self._expense_claims

    @expense_claims.setter
    def expense_claims(self, expense_claims):
        """Sets the expense_claims of this ExpenseClaims.


        :param expense_claims: The expense_claims of this ExpenseClaims.  # noqa: E501
        :type: list[ExpenseClaim]
        """

        self._expense_claims = expense_claims
