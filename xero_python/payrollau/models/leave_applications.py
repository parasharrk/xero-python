# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    OpenAPI spec version: 2.3.0
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class LeaveApplications(BaseModel):
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
    openapi_types = {"leave_applications": "list[LeaveApplication]"}

    attribute_map = {"leave_applications": "LeaveApplications"}

    def __init__(self, leave_applications=None):  # noqa: E501
        """LeaveApplications - a model defined in OpenAPI"""  # noqa: E501

        self._leave_applications = None
        self.discriminator = None

        if leave_applications is not None:
            self.leave_applications = leave_applications

    @property
    def leave_applications(self):
        """Gets the leave_applications of this LeaveApplications.  # noqa: E501


        :return: The leave_applications of this LeaveApplications.  # noqa: E501
        :rtype: list[LeaveApplication]
        """
        return self._leave_applications

    @leave_applications.setter
    def leave_applications(self, leave_applications):
        """Sets the leave_applications of this LeaveApplications.


        :param leave_applications: The leave_applications of this LeaveApplications.  # noqa: E501
        :type: list[LeaveApplication]
        """

        self._leave_applications = leave_applications
