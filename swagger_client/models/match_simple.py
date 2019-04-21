# coding: utf-8

"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.  # noqa: E501

    OpenAPI spec version: 3.04.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.match_simple_alliances import MatchSimpleAlliances  # noqa: F401,E501


class MatchSimple(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'key': 'str',
        'comp_level': 'str',
        'set_number': 'int',
        'match_number': 'int',
        'alliances': 'MatchSimpleAlliances',
        'winning_alliance': 'str',
        'event_key': 'str',
        'time': 'int',
        'predicted_time': 'int',
        'actual_time': 'int'
    }

    attribute_map = {
        'key': 'key',
        'comp_level': 'comp_level',
        'set_number': 'set_number',
        'match_number': 'match_number',
        'alliances': 'alliances',
        'winning_alliance': 'winning_alliance',
        'event_key': 'event_key',
        'time': 'time',
        'predicted_time': 'predicted_time',
        'actual_time': 'actual_time'
    }

    def __init__(self, key=None, comp_level=None, set_number=None, match_number=None, alliances=None, winning_alliance=None, event_key=None, time=None, predicted_time=None, actual_time=None):  # noqa: E501
        """MatchSimple - a model defined in Swagger"""  # noqa: E501

        self._key = None
        self._comp_level = None
        self._set_number = None
        self._match_number = None
        self._alliances = None
        self._winning_alliance = None
        self._event_key = None
        self._time = None
        self._predicted_time = None
        self._actual_time = None
        self.discriminator = None

        self.key = key
        self.comp_level = comp_level
        self.set_number = set_number
        self.match_number = match_number
        if alliances is not None:
            self.alliances = alliances
        if winning_alliance is not None:
            self.winning_alliance = winning_alliance
        self.event_key = event_key
        if time is not None:
            self.time = time
        if predicted_time is not None:
            self.predicted_time = predicted_time
        if actual_time is not None:
            self.actual_time = actual_time

    @property
    def key(self):
        """Gets the key of this MatchSimple.  # noqa: E501

        TBA match key with the format `yyyy[EVENT_CODE]_[COMP_LEVEL]m[MATCH_NUMBER]`, where `yyyy` is the year, and `EVENT_CODE` is the event code of the event, `COMP_LEVEL` is (qm, ef, qf, sf, f), and `MATCH_NUMBER` is the match number in the competition level. A set number may append the competition level if more than one match in required per set.  # noqa: E501

        :return: The key of this MatchSimple.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this MatchSimple.

        TBA match key with the format `yyyy[EVENT_CODE]_[COMP_LEVEL]m[MATCH_NUMBER]`, where `yyyy` is the year, and `EVENT_CODE` is the event code of the event, `COMP_LEVEL` is (qm, ef, qf, sf, f), and `MATCH_NUMBER` is the match number in the competition level. A set number may append the competition level if more than one match in required per set.  # noqa: E501

        :param key: The key of this MatchSimple.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def comp_level(self):
        """Gets the comp_level of this MatchSimple.  # noqa: E501

        The competition level the match was played at.  # noqa: E501

        :return: The comp_level of this MatchSimple.  # noqa: E501
        :rtype: str
        """
        return self._comp_level

    @comp_level.setter
    def comp_level(self, comp_level):
        """Sets the comp_level of this MatchSimple.

        The competition level the match was played at.  # noqa: E501

        :param comp_level: The comp_level of this MatchSimple.  # noqa: E501
        :type: str
        """
        if comp_level is None:
            raise ValueError("Invalid value for `comp_level`, must not be `None`")  # noqa: E501
        allowed_values = ["qm", "ef", "qf", "sf", "f"]  # noqa: E501
        if comp_level not in allowed_values:
            raise ValueError(
                "Invalid value for `comp_level` ({0}), must be one of {1}"  # noqa: E501
                .format(comp_level, allowed_values)
            )

        self._comp_level = comp_level

    @property
    def set_number(self):
        """Gets the set_number of this MatchSimple.  # noqa: E501

        The set number in a series of matches where more than one match is required in the match series.  # noqa: E501

        :return: The set_number of this MatchSimple.  # noqa: E501
        :rtype: int
        """
        return self._set_number

    @set_number.setter
    def set_number(self, set_number):
        """Sets the set_number of this MatchSimple.

        The set number in a series of matches where more than one match is required in the match series.  # noqa: E501

        :param set_number: The set_number of this MatchSimple.  # noqa: E501
        :type: int
        """
        if set_number is None:
            raise ValueError("Invalid value for `set_number`, must not be `None`")  # noqa: E501

        self._set_number = set_number

    @property
    def match_number(self):
        """Gets the match_number of this MatchSimple.  # noqa: E501

        The match number of the match in the competition level.  # noqa: E501

        :return: The match_number of this MatchSimple.  # noqa: E501
        :rtype: int
        """
        return self._match_number

    @match_number.setter
    def match_number(self, match_number):
        """Sets the match_number of this MatchSimple.

        The match number of the match in the competition level.  # noqa: E501

        :param match_number: The match_number of this MatchSimple.  # noqa: E501
        :type: int
        """
        if match_number is None:
            raise ValueError("Invalid value for `match_number`, must not be `None`")  # noqa: E501

        self._match_number = match_number

    @property
    def alliances(self):
        """Gets the alliances of this MatchSimple.  # noqa: E501


        :return: The alliances of this MatchSimple.  # noqa: E501
        :rtype: MatchSimpleAlliances
        """
        return self._alliances

    @alliances.setter
    def alliances(self, alliances):
        """Sets the alliances of this MatchSimple.


        :param alliances: The alliances of this MatchSimple.  # noqa: E501
        :type: MatchSimpleAlliances
        """

        self._alliances = alliances

    @property
    def winning_alliance(self):
        """Gets the winning_alliance of this MatchSimple.  # noqa: E501

        The color (red/blue) of the winning alliance. Will contain an empty string in the event of no winner, or a tie.  # noqa: E501

        :return: The winning_alliance of this MatchSimple.  # noqa: E501
        :rtype: str
        """
        return self._winning_alliance

    @winning_alliance.setter
    def winning_alliance(self, winning_alliance):
        """Sets the winning_alliance of this MatchSimple.

        The color (red/blue) of the winning alliance. Will contain an empty string in the event of no winner, or a tie.  # noqa: E501

        :param winning_alliance: The winning_alliance of this MatchSimple.  # noqa: E501
        :type: str
        """
        allowed_values = ["red", "blue"]  # noqa: E501
        if winning_alliance not in allowed_values:
            raise ValueError(
                "Invalid value for `winning_alliance` ({0}), must be one of {1}"  # noqa: E501
                .format(winning_alliance, allowed_values)
            )

        self._winning_alliance = winning_alliance

    @property
    def event_key(self):
        """Gets the event_key of this MatchSimple.  # noqa: E501

        Event key of the event the match was played at.  # noqa: E501

        :return: The event_key of this MatchSimple.  # noqa: E501
        :rtype: str
        """
        return self._event_key

    @event_key.setter
    def event_key(self, event_key):
        """Sets the event_key of this MatchSimple.

        Event key of the event the match was played at.  # noqa: E501

        :param event_key: The event_key of this MatchSimple.  # noqa: E501
        :type: str
        """
        if event_key is None:
            raise ValueError("Invalid value for `event_key`, must not be `None`")  # noqa: E501

        self._event_key = event_key

    @property
    def time(self):
        """Gets the time of this MatchSimple.  # noqa: E501

        UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of the scheduled match time, as taken from the published schedule.  # noqa: E501

        :return: The time of this MatchSimple.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this MatchSimple.

        UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of the scheduled match time, as taken from the published schedule.  # noqa: E501

        :param time: The time of this MatchSimple.  # noqa: E501
        :type: int
        """

        self._time = time

    @property
    def predicted_time(self):
        """Gets the predicted_time of this MatchSimple.  # noqa: E501

        UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of the TBA predicted match start time.  # noqa: E501

        :return: The predicted_time of this MatchSimple.  # noqa: E501
        :rtype: int
        """
        return self._predicted_time

    @predicted_time.setter
    def predicted_time(self, predicted_time):
        """Sets the predicted_time of this MatchSimple.

        UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of the TBA predicted match start time.  # noqa: E501

        :param predicted_time: The predicted_time of this MatchSimple.  # noqa: E501
        :type: int
        """

        self._predicted_time = predicted_time

    @property
    def actual_time(self):
        """Gets the actual_time of this MatchSimple.  # noqa: E501

        UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of actual match start time.  # noqa: E501

        :return: The actual_time of this MatchSimple.  # noqa: E501
        :rtype: int
        """
        return self._actual_time

    @actual_time.setter
    def actual_time(self, actual_time):
        """Sets the actual_time of this MatchSimple.

        UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of actual match start time.  # noqa: E501

        :param actual_time: The actual_time of this MatchSimple.  # noqa: E501
        :type: int
        """

        self._actual_time = actual_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MatchSimple, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MatchSimple):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
