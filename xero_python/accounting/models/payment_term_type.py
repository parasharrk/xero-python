# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.3.0
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from enum import Enum


class PaymentTermType(Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    allowed enum values
    """

    DAYSAFTERBILLDATE = "DAYSAFTERBILLDATE"
    DAYSAFTERBILLMONTH = "DAYSAFTERBILLMONTH"
    OFCURRENTMONTH = "OFCURRENTMONTH"
    OFFOLLOWINGMONTH = "OFFOLLOWINGMONTH"
