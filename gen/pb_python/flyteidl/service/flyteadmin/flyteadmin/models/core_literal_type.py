# coding: utf-8

"""
    flyteidl/service/admin.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flyteadmin.models.core_blob_type import CoreBlobType  # noqa: F401,E501
from flyteadmin.models.core_enum_type import CoreEnumType  # noqa: F401,E501
from flyteadmin.models.core_literal_type import CoreLiteralType  # noqa: F401,E501
from flyteadmin.models.core_schema_type import CoreSchemaType  # noqa: F401,E501
from flyteadmin.models.core_simple_type import CoreSimpleType  # noqa: F401,E501
from flyteadmin.models.protobuf_struct import ProtobufStruct  # noqa: F401,E501


class CoreLiteralType(object):
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
        'simple': 'CoreSimpleType',
        'schema': 'CoreSchemaType',
        'collection_type': 'CoreLiteralType',
        'map_value_type': 'CoreLiteralType',
        'blob': 'CoreBlobType',
        'enum_type': 'CoreEnumType',
        'metadata': 'ProtobufStruct'
    }

    attribute_map = {
        'simple': 'simple',
        'schema': 'schema',
        'collection_type': 'collection_type',
        'map_value_type': 'map_value_type',
        'blob': 'blob',
        'enum_type': 'enum_type',
        'metadata': 'metadata'
    }

    def __init__(self, simple=None, schema=None, collection_type=None, map_value_type=None, blob=None, enum_type=None, metadata=None):  # noqa: E501
        """CoreLiteralType - a model defined in Swagger"""  # noqa: E501

        self._simple = None
        self._schema = None
        self._collection_type = None
        self._map_value_type = None
        self._blob = None
        self._enum_type = None
        self._metadata = None
        self.discriminator = None

        if simple is not None:
            self.simple = simple
        if schema is not None:
            self.schema = schema
        if collection_type is not None:
            self.collection_type = collection_type
        if map_value_type is not None:
            self.map_value_type = map_value_type
        if blob is not None:
            self.blob = blob
        if enum_type is not None:
            self.enum_type = enum_type
        if metadata is not None:
            self.metadata = metadata

    @property
    def simple(self):
        """Gets the simple of this CoreLiteralType.  # noqa: E501

        A simple type that can be compared one-to-one with another.  # noqa: E501

        :return: The simple of this CoreLiteralType.  # noqa: E501
        :rtype: CoreSimpleType
        """
        return self._simple

    @simple.setter
    def simple(self, simple):
        """Sets the simple of this CoreLiteralType.

        A simple type that can be compared one-to-one with another.  # noqa: E501

        :param simple: The simple of this CoreLiteralType.  # noqa: E501
        :type: CoreSimpleType
        """

        self._simple = simple

    @property
    def schema(self):
        """Gets the schema of this CoreLiteralType.  # noqa: E501

        A complex type that requires matching of inner fields.  # noqa: E501

        :return: The schema of this CoreLiteralType.  # noqa: E501
        :rtype: CoreSchemaType
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this CoreLiteralType.

        A complex type that requires matching of inner fields.  # noqa: E501

        :param schema: The schema of this CoreLiteralType.  # noqa: E501
        :type: CoreSchemaType
        """

        self._schema = schema

    @property
    def collection_type(self):
        """Gets the collection_type of this CoreLiteralType.  # noqa: E501

        Defines the type of the value of a collection. Only homogeneous collections are allowed.  # noqa: E501

        :return: The collection_type of this CoreLiteralType.  # noqa: E501
        :rtype: CoreLiteralType
        """
        return self._collection_type

    @collection_type.setter
    def collection_type(self, collection_type):
        """Sets the collection_type of this CoreLiteralType.

        Defines the type of the value of a collection. Only homogeneous collections are allowed.  # noqa: E501

        :param collection_type: The collection_type of this CoreLiteralType.  # noqa: E501
        :type: CoreLiteralType
        """

        self._collection_type = collection_type

    @property
    def map_value_type(self):
        """Gets the map_value_type of this CoreLiteralType.  # noqa: E501

        Defines the type of the value of a map type. The type of the key is always a string.  # noqa: E501

        :return: The map_value_type of this CoreLiteralType.  # noqa: E501
        :rtype: CoreLiteralType
        """
        return self._map_value_type

    @map_value_type.setter
    def map_value_type(self, map_value_type):
        """Sets the map_value_type of this CoreLiteralType.

        Defines the type of the value of a map type. The type of the key is always a string.  # noqa: E501

        :param map_value_type: The map_value_type of this CoreLiteralType.  # noqa: E501
        :type: CoreLiteralType
        """

        self._map_value_type = map_value_type

    @property
    def blob(self):
        """Gets the blob of this CoreLiteralType.  # noqa: E501

        A blob might have specialized implementation details depending on associated metadata.  # noqa: E501

        :return: The blob of this CoreLiteralType.  # noqa: E501
        :rtype: CoreBlobType
        """
        return self._blob

    @blob.setter
    def blob(self, blob):
        """Sets the blob of this CoreLiteralType.

        A blob might have specialized implementation details depending on associated metadata.  # noqa: E501

        :param blob: The blob of this CoreLiteralType.  # noqa: E501
        :type: CoreBlobType
        """

        self._blob = blob

    @property
    def enum_type(self):
        """Gets the enum_type of this CoreLiteralType.  # noqa: E501

        Defines an enum with pre-defined string values.  # noqa: E501

        :return: The enum_type of this CoreLiteralType.  # noqa: E501
        :rtype: CoreEnumType
        """
        return self._enum_type

    @enum_type.setter
    def enum_type(self, enum_type):
        """Sets the enum_type of this CoreLiteralType.

        Defines an enum with pre-defined string values.  # noqa: E501

        :param enum_type: The enum_type of this CoreLiteralType.  # noqa: E501
        :type: CoreEnumType
        """

        self._enum_type = enum_type

    @property
    def metadata(self):
        """Gets the metadata of this CoreLiteralType.  # noqa: E501

        This field contains type metadata that is descriptive of the type, but is NOT considered in type-checking.  This might be used by consumers to identify special behavior or display extended information for the type.  # noqa: E501

        :return: The metadata of this CoreLiteralType.  # noqa: E501
        :rtype: ProtobufStruct
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CoreLiteralType.

        This field contains type metadata that is descriptive of the type, but is NOT considered in type-checking.  This might be used by consumers to identify special behavior or display extended information for the type.  # noqa: E501

        :param metadata: The metadata of this CoreLiteralType.  # noqa: E501
        :type: ProtobufStruct
        """

        self._metadata = metadata

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
        if issubclass(CoreLiteralType, dict):
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
        if not isinstance(other, CoreLiteralType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
