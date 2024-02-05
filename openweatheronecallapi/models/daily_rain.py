# -*- coding: utf-8 -*-

"""
openweatheronecallapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from openweatheronecallapi.api_helper import APIHelper


class DailyRain(object):

    """Implementation of the 'DailyRain' model.

    Minute weather measurements

    Attributes:
        m_1_h (float): (where available) Precipitation, mm/h. Please note that
            only mm/h as units of measurement are available for this
            parameter

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "m_1_h": '1h'
    }

    _optionals = [
        'm_1_h',
    ]

    def __init__(self,
                 m_1_h=APIHelper.SKIP):
        """Constructor for the DailyRain class"""

        # Initialize members of the class
        if m_1_h is not APIHelper.SKIP:
            self.m_1_h = m_1_h 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        m_1_h = dictionary.get("1h") if dictionary.get("1h") else APIHelper.SKIP
        # Return an object of this model
        return cls(m_1_h)
