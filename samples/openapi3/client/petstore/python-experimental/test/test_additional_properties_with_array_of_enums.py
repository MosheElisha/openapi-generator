# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import petstore_api
try:
    from petstore_api.model import enum_class
except ImportError:
    enum_class = sys.modules[
        'petstore_api.model.enum_class']
from petstore_api.model.additional_properties_with_array_of_enums import AdditionalPropertiesWithArrayOfEnums


class TestAdditionalPropertiesWithArrayOfEnums(unittest.TestCase):
    """AdditionalPropertiesWithArrayOfEnums unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAdditionalPropertiesWithArrayOfEnums(self):
        """Test AdditionalPropertiesWithArrayOfEnums"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AdditionalPropertiesWithArrayOfEnums()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
