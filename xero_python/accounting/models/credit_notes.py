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


class CreditNotes(BaseModel):
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
    openapi_types = {"credit_notes": "list[CreditNote]"}

    attribute_map = {"credit_notes": "CreditNotes"}

    def __init__(self, credit_notes=None):  # noqa: E501
        """CreditNotes - a model defined in OpenAPI"""  # noqa: E501

        self._credit_notes = None
        self.discriminator = None

        if credit_notes is not None:
            self.credit_notes = credit_notes

    @property
    def credit_notes(self):
        """Gets the credit_notes of this CreditNotes.  # noqa: E501


        :return: The credit_notes of this CreditNotes.  # noqa: E501
        :rtype: list[CreditNote]
        """
        return self._credit_notes

    @credit_notes.setter
    def credit_notes(self, credit_notes):
        """Sets the credit_notes of this CreditNotes.


        :param credit_notes: The credit_notes of this CreditNotes.  # noqa: E501
        :type: list[CreditNote]
        """

        self._credit_notes = credit_notes
