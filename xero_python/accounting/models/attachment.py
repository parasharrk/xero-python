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


class Attachment(BaseModel):
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
        "attachment_id": "str",
        "file_name": "str",
        "url": "str",
        "mime_type": "str",
        "content_length": "int",
        "include_online": "bool",
    }

    attribute_map = {
        "attachment_id": "AttachmentID",
        "file_name": "FileName",
        "url": "Url",
        "mime_type": "MimeType",
        "content_length": "ContentLength",
        "include_online": "IncludeOnline",
    }

    def __init__(
        self,
        attachment_id=None,
        file_name=None,
        url=None,
        mime_type=None,
        content_length=None,
        include_online=None,
    ):  # noqa: E501
        """Attachment - a model defined in OpenAPI"""  # noqa: E501

        self._attachment_id = None
        self._file_name = None
        self._url = None
        self._mime_type = None
        self._content_length = None
        self._include_online = None
        self.discriminator = None

        if attachment_id is not None:
            self.attachment_id = attachment_id
        if file_name is not None:
            self.file_name = file_name
        if url is not None:
            self.url = url
        if mime_type is not None:
            self.mime_type = mime_type
        if content_length is not None:
            self.content_length = content_length
        if include_online is not None:
            self.include_online = include_online

    @property
    def attachment_id(self):
        """Gets the attachment_id of this Attachment.  # noqa: E501

        Unique ID for the file  # noqa: E501

        :return: The attachment_id of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        """Sets the attachment_id of this Attachment.

        Unique ID for the file  # noqa: E501

        :param attachment_id: The attachment_id of this Attachment.  # noqa: E501
        :type: str
        """

        self._attachment_id = attachment_id

    @property
    def file_name(self):
        """Gets the file_name of this Attachment.  # noqa: E501

        Name of the file  # noqa: E501

        :return: The file_name of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this Attachment.

        Name of the file  # noqa: E501

        :param file_name: The file_name of this Attachment.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def url(self):
        """Gets the url of this Attachment.  # noqa: E501

        URL to the file on xero.com  # noqa: E501

        :return: The url of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Attachment.

        URL to the file on xero.com  # noqa: E501

        :param url: The url of this Attachment.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def mime_type(self):
        """Gets the mime_type of this Attachment.  # noqa: E501

        Type of file  # noqa: E501

        :return: The mime_type of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this Attachment.

        Type of file  # noqa: E501

        :param mime_type: The mime_type of this Attachment.  # noqa: E501
        :type: str
        """

        self._mime_type = mime_type

    @property
    def content_length(self):
        """Gets the content_length of this Attachment.  # noqa: E501

        Length of the file content  # noqa: E501

        :return: The content_length of this Attachment.  # noqa: E501
        :rtype: int
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this Attachment.

        Length of the file content  # noqa: E501

        :param content_length: The content_length of this Attachment.  # noqa: E501
        :type: int
        """

        self._content_length = content_length

    @property
    def include_online(self):
        """Gets the include_online of this Attachment.  # noqa: E501

        Include the file with the online invoice  # noqa: E501

        :return: The include_online of this Attachment.  # noqa: E501
        :rtype: bool
        """
        return self._include_online

    @include_online.setter
    def include_online(self, include_online):
        """Sets the include_online of this Attachment.

        Include the file with the online invoice  # noqa: E501

        :param include_online: The include_online of this Attachment.  # noqa: E501
        :type: bool
        """

        self._include_online = include_online
