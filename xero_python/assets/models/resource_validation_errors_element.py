# coding: utf-8

"""
    Xero Assets API

    This is the Xero Assets API  # noqa: E501

    OpenAPI spec version: 2.3.0
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class ResourceValidationErrorsElement(BaseModel):
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
        "resource_name": "str",
        "localised_message": "str",
        "type": "str",
        "title": "str",
        "detail": "str",
    }

    attribute_map = {
        "resource_name": "resourceName",
        "localised_message": "localisedMessage",
        "type": "type",
        "title": "title",
        "detail": "detail",
    }

    def __init__(
        self,
        resource_name=None,
        localised_message=None,
        type=None,
        title=None,
        detail=None,
    ):  # noqa: E501
        """ResourceValidationErrorsElement - a model defined in OpenAPI"""  # noqa: E501

        self._resource_name = None
        self._localised_message = None
        self._type = None
        self._title = None
        self._detail = None
        self.discriminator = None

        if resource_name is not None:
            self.resource_name = resource_name
        if localised_message is not None:
            self.localised_message = localised_message
        if type is not None:
            self.type = type
        if title is not None:
            self.title = title
        if detail is not None:
            self.detail = detail

    @property
    def resource_name(self):
        """Gets the resource_name of this ResourceValidationErrorsElement.  # noqa: E501

        The field name of the erroneous field  # noqa: E501

        :return: The resource_name of this ResourceValidationErrorsElement.  # noqa: E501
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ResourceValidationErrorsElement.

        The field name of the erroneous field  # noqa: E501

        :param resource_name: The resource_name of this ResourceValidationErrorsElement.  # noqa: E501
        :type: str
        """

        self._resource_name = resource_name

    @property
    def localised_message(self):
        """Gets the localised_message of this ResourceValidationErrorsElement.  # noqa: E501

        Explaination of the resource validation error  # noqa: E501

        :return: The localised_message of this ResourceValidationErrorsElement.  # noqa: E501
        :rtype: str
        """
        return self._localised_message

    @localised_message.setter
    def localised_message(self, localised_message):
        """Sets the localised_message of this ResourceValidationErrorsElement.

        Explaination of the resource validation error  # noqa: E501

        :param localised_message: The localised_message of this ResourceValidationErrorsElement.  # noqa: E501
        :type: str
        """

        self._localised_message = localised_message

    @property
    def type(self):
        """Gets the type of this ResourceValidationErrorsElement.  # noqa: E501

        Internal type of the resource error message  # noqa: E501

        :return: The type of this ResourceValidationErrorsElement.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceValidationErrorsElement.

        Internal type of the resource error message  # noqa: E501

        :param type: The type of this ResourceValidationErrorsElement.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def title(self):
        """Gets the title of this ResourceValidationErrorsElement.  # noqa: E501

        Title of the resource validation error  # noqa: E501

        :return: The title of this ResourceValidationErrorsElement.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ResourceValidationErrorsElement.

        Title of the resource validation error  # noqa: E501

        :param title: The title of this ResourceValidationErrorsElement.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def detail(self):
        """Gets the detail of this ResourceValidationErrorsElement.  # noqa: E501

        Detail of the resource validation error  # noqa: E501

        :return: The detail of this ResourceValidationErrorsElement.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ResourceValidationErrorsElement.

        Detail of the resource validation error  # noqa: E501

        :param detail: The detail of this ResourceValidationErrorsElement.  # noqa: E501
        :type: str
        """

        self._detail = detail
