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


class Setting(BaseModel):
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
        "asset_number_prefix": "str",
        "asset_number_sequence": "str",
        "asset_start_date": "date",
        "last_depreciation_date": "date",
        "default_gain_on_disposal_account_id": "str",
        "default_loss_on_disposal_account_id": "str",
        "default_capital_gain_on_disposal_account_id": "str",
        "opt_in_for_tax": "bool",
    }

    attribute_map = {
        "asset_number_prefix": "assetNumberPrefix",
        "asset_number_sequence": "assetNumberSequence",
        "asset_start_date": "assetStartDate",
        "last_depreciation_date": "lastDepreciationDate",
        "default_gain_on_disposal_account_id": "defaultGainOnDisposalAccountId",
        "default_loss_on_disposal_account_id": "defaultLossOnDisposalAccountId",
        "default_capital_gain_on_disposal_account_id": "defaultCapitalGainOnDisposalAccountId",
        "opt_in_for_tax": "optInForTax",
    }

    def __init__(
        self,
        asset_number_prefix=None,
        asset_number_sequence=None,
        asset_start_date=None,
        last_depreciation_date=None,
        default_gain_on_disposal_account_id=None,
        default_loss_on_disposal_account_id=None,
        default_capital_gain_on_disposal_account_id=None,
        opt_in_for_tax=None,
    ):  # noqa: E501
        """Setting - a model defined in OpenAPI"""  # noqa: E501

        self._asset_number_prefix = None
        self._asset_number_sequence = None
        self._asset_start_date = None
        self._last_depreciation_date = None
        self._default_gain_on_disposal_account_id = None
        self._default_loss_on_disposal_account_id = None
        self._default_capital_gain_on_disposal_account_id = None
        self._opt_in_for_tax = None
        self.discriminator = None

        if asset_number_prefix is not None:
            self.asset_number_prefix = asset_number_prefix
        if asset_number_sequence is not None:
            self.asset_number_sequence = asset_number_sequence
        if asset_start_date is not None:
            self.asset_start_date = asset_start_date
        if last_depreciation_date is not None:
            self.last_depreciation_date = last_depreciation_date
        if default_gain_on_disposal_account_id is not None:
            self.default_gain_on_disposal_account_id = (
                default_gain_on_disposal_account_id
            )
        if default_loss_on_disposal_account_id is not None:
            self.default_loss_on_disposal_account_id = (
                default_loss_on_disposal_account_id
            )
        if default_capital_gain_on_disposal_account_id is not None:
            self.default_capital_gain_on_disposal_account_id = (
                default_capital_gain_on_disposal_account_id
            )
        if opt_in_for_tax is not None:
            self.opt_in_for_tax = opt_in_for_tax

    @property
    def asset_number_prefix(self):
        """Gets the asset_number_prefix of this Setting.  # noqa: E501

        The prefix used for fixed asset numbers (“FA-” by default)  # noqa: E501

        :return: The asset_number_prefix of this Setting.  # noqa: E501
        :rtype: str
        """
        return self._asset_number_prefix

    @asset_number_prefix.setter
    def asset_number_prefix(self, asset_number_prefix):
        """Sets the asset_number_prefix of this Setting.

        The prefix used for fixed asset numbers (“FA-” by default)  # noqa: E501

        :param asset_number_prefix: The asset_number_prefix of this Setting.  # noqa: E501
        :type: str
        """

        self._asset_number_prefix = asset_number_prefix

    @property
    def asset_number_sequence(self):
        """Gets the asset_number_sequence of this Setting.  # noqa: E501

        The next available sequence number  # noqa: E501

        :return: The asset_number_sequence of this Setting.  # noqa: E501
        :rtype: str
        """
        return self._asset_number_sequence

    @asset_number_sequence.setter
    def asset_number_sequence(self, asset_number_sequence):
        """Sets the asset_number_sequence of this Setting.

        The next available sequence number  # noqa: E501

        :param asset_number_sequence: The asset_number_sequence of this Setting.  # noqa: E501
        :type: str
        """

        self._asset_number_sequence = asset_number_sequence

    @property
    def asset_start_date(self):
        """Gets the asset_start_date of this Setting.  # noqa: E501

        The date depreciation calculations started on registered fixed assets in Xero  # noqa: E501

        :return: The asset_start_date of this Setting.  # noqa: E501
        :rtype: date
        """
        return self._asset_start_date

    @asset_start_date.setter
    def asset_start_date(self, asset_start_date):
        """Sets the asset_start_date of this Setting.

        The date depreciation calculations started on registered fixed assets in Xero  # noqa: E501

        :param asset_start_date: The asset_start_date of this Setting.  # noqa: E501
        :type: date
        """

        self._asset_start_date = asset_start_date

    @property
    def last_depreciation_date(self):
        """Gets the last_depreciation_date of this Setting.  # noqa: E501

        The last depreciation date  # noqa: E501

        :return: The last_depreciation_date of this Setting.  # noqa: E501
        :rtype: date
        """
        return self._last_depreciation_date

    @last_depreciation_date.setter
    def last_depreciation_date(self, last_depreciation_date):
        """Sets the last_depreciation_date of this Setting.

        The last depreciation date  # noqa: E501

        :param last_depreciation_date: The last_depreciation_date of this Setting.  # noqa: E501
        :type: date
        """

        self._last_depreciation_date = last_depreciation_date

    @property
    def default_gain_on_disposal_account_id(self):
        """Gets the default_gain_on_disposal_account_id of this Setting.  # noqa: E501

        Default account that gains are posted to  # noqa: E501

        :return: The default_gain_on_disposal_account_id of this Setting.  # noqa: E501
        :rtype: str
        """
        return self._default_gain_on_disposal_account_id

    @default_gain_on_disposal_account_id.setter
    def default_gain_on_disposal_account_id(self, default_gain_on_disposal_account_id):
        """Sets the default_gain_on_disposal_account_id of this Setting.

        Default account that gains are posted to  # noqa: E501

        :param default_gain_on_disposal_account_id: The default_gain_on_disposal_account_id of this Setting.  # noqa: E501
        :type: str
        """

        self._default_gain_on_disposal_account_id = default_gain_on_disposal_account_id

    @property
    def default_loss_on_disposal_account_id(self):
        """Gets the default_loss_on_disposal_account_id of this Setting.  # noqa: E501

        Default account that losses are posted to  # noqa: E501

        :return: The default_loss_on_disposal_account_id of this Setting.  # noqa: E501
        :rtype: str
        """
        return self._default_loss_on_disposal_account_id

    @default_loss_on_disposal_account_id.setter
    def default_loss_on_disposal_account_id(self, default_loss_on_disposal_account_id):
        """Sets the default_loss_on_disposal_account_id of this Setting.

        Default account that losses are posted to  # noqa: E501

        :param default_loss_on_disposal_account_id: The default_loss_on_disposal_account_id of this Setting.  # noqa: E501
        :type: str
        """

        self._default_loss_on_disposal_account_id = default_loss_on_disposal_account_id

    @property
    def default_capital_gain_on_disposal_account_id(self):
        """Gets the default_capital_gain_on_disposal_account_id of this Setting.  # noqa: E501

        Default account that capital gains are posted to  # noqa: E501

        :return: The default_capital_gain_on_disposal_account_id of this Setting.  # noqa: E501
        :rtype: str
        """
        return self._default_capital_gain_on_disposal_account_id

    @default_capital_gain_on_disposal_account_id.setter
    def default_capital_gain_on_disposal_account_id(
        self, default_capital_gain_on_disposal_account_id
    ):
        """Sets the default_capital_gain_on_disposal_account_id of this Setting.

        Default account that capital gains are posted to  # noqa: E501

        :param default_capital_gain_on_disposal_account_id: The default_capital_gain_on_disposal_account_id of this Setting.  # noqa: E501
        :type: str
        """

        self._default_capital_gain_on_disposal_account_id = (
            default_capital_gain_on_disposal_account_id
        )

    @property
    def opt_in_for_tax(self):
        """Gets the opt_in_for_tax of this Setting.  # noqa: E501

        opt in for tax calculation  # noqa: E501

        :return: The opt_in_for_tax of this Setting.  # noqa: E501
        :rtype: bool
        """
        return self._opt_in_for_tax

    @opt_in_for_tax.setter
    def opt_in_for_tax(self, opt_in_for_tax):
        """Sets the opt_in_for_tax of this Setting.

        opt in for tax calculation  # noqa: E501

        :param opt_in_for_tax: The opt_in_for_tax of this Setting.  # noqa: E501
        :type: bool
        """

        self._opt_in_for_tax = opt_in_for_tax
