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


class Attachments(BaseModel):
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
    openapi_types = {"attachments": "list[Attachment]"}

    attribute_map = {"attachments": "Attachments"}

    def __init__(self, attachments=None):  # noqa: E501
        """Attachments - a model defined in OpenAPI"""  # noqa: E501

        self._attachments = None
        self.discriminator = None

        if attachments is not None:
            self.attachments = attachments

    @property
    def attachments(self):
        """Gets the attachments of this Attachments.  # noqa: E501


        :return: The attachments of this Attachments.  # noqa: E501
        :rtype: list[Attachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this Attachments.


        :param attachments: The attachments of this Attachments.  # noqa: E501
        :type: list[Attachment]
        """

        self._attachments = attachments
