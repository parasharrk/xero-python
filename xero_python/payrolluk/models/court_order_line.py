# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    OpenAPI spec version: 2.3.0
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class CourtOrderLine(BaseModel):
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
    openapi_types = {"court_order_type_id": "str", "amount": "float"}

    attribute_map = {"court_order_type_id": "courtOrderTypeID", "amount": "amount"}

    def __init__(self, court_order_type_id=None, amount=None):  # noqa: E501
        """CourtOrderLine - a model defined in OpenAPI"""  # noqa: E501

        self._court_order_type_id = None
        self._amount = None
        self.discriminator = None

        if court_order_type_id is not None:
            self.court_order_type_id = court_order_type_id
        if amount is not None:
            self.amount = amount

    @property
    def court_order_type_id(self):
        """Gets the court_order_type_id of this CourtOrderLine.  # noqa: E501

        Xero identifier for payroll court order type  # noqa: E501

        :return: The court_order_type_id of this CourtOrderLine.  # noqa: E501
        :rtype: str
        """
        return self._court_order_type_id

    @court_order_type_id.setter
    def court_order_type_id(self, court_order_type_id):
        """Sets the court_order_type_id of this CourtOrderLine.

        Xero identifier for payroll court order type  # noqa: E501

        :param court_order_type_id: The court_order_type_id of this CourtOrderLine.  # noqa: E501
        :type: str
        """

        self._court_order_type_id = court_order_type_id

    @property
    def amount(self):
        """Gets the amount of this CourtOrderLine.  # noqa: E501

        Amount  # noqa: E501

        :return: The amount of this CourtOrderLine.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CourtOrderLine.

        Amount  # noqa: E501

        :param amount: The amount of this CourtOrderLine.  # noqa: E501
        :type: float
        """

        self._amount = amount
