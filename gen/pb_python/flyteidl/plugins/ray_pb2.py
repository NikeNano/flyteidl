# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/plugins/ray.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flyteidl/plugins/ray.proto',
  package='flyteidl.plugins',
  syntax='proto3',
  serialized_options=_b('Z7github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/plugins'),
  serialized_pb=_b('\n\x1a\x66lyteidl/plugins/ray.proto\x12\x10\x66lyteidl.plugins\x1a\x1fgoogle/protobuf/timestamp.proto\"P\n\x06RayJob\x12\x31\n\x0bray_cluster\x18\x01 \x01(\x0b\x32\x1c.flyteidl.plugins.RayCluster\x12\x13\n\x0bruntime_env\x18\x02 \x01(\t\"\x84\x01\n\nRayCluster\x12\x38\n\x0fhead_group_spec\x18\x01 \x01(\x0b\x32\x1f.flyteidl.plugins.HeadGroupSpec\x12<\n\x11worker_group_spec\x18\x02 \x03(\x0b\x32!.flyteidl.plugins.WorkerGroupSpec\"\x95\x01\n\rHeadGroupSpec\x12M\n\x10ray_start_params\x18\x01 \x03(\x0b\x32\x33.flyteidl.plugins.HeadGroupSpec.RayStartParamsEntry\x1a\x35\n\x13RayStartParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xeb\x01\n\x0fWorkerGroupSpec\x12\x12\n\ngroup_name\x18\x01 \x01(\t\x12\x10\n\x08replicas\x18\x02 \x01(\x05\x12\x14\n\x0cmin_replicas\x18\x03 \x01(\x05\x12\x14\n\x0cmax_replicas\x18\x04 \x01(\x05\x12O\n\x10ray_start_params\x18\x05 \x03(\x0b\x32\x35.flyteidl.plugins.WorkerGroupSpec.RayStartParamsEntry\x1a\x35\n\x13RayStartParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x39Z7github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/pluginsb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_RAYJOB = _descriptor.Descriptor(
  name='RayJob',
  full_name='flyteidl.plugins.RayJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ray_cluster', full_name='flyteidl.plugins.RayJob.ray_cluster', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='runtime_env', full_name='flyteidl.plugins.RayJob.runtime_env', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=161,
)


_RAYCLUSTER = _descriptor.Descriptor(
  name='RayCluster',
  full_name='flyteidl.plugins.RayCluster',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='head_group_spec', full_name='flyteidl.plugins.RayCluster.head_group_spec', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='worker_group_spec', full_name='flyteidl.plugins.RayCluster.worker_group_spec', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=296,
)


_HEADGROUPSPEC_RAYSTARTPARAMSENTRY = _descriptor.Descriptor(
  name='RayStartParamsEntry',
  full_name='flyteidl.plugins.HeadGroupSpec.RayStartParamsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='flyteidl.plugins.HeadGroupSpec.RayStartParamsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='flyteidl.plugins.HeadGroupSpec.RayStartParamsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=395,
  serialized_end=448,
)

_HEADGROUPSPEC = _descriptor.Descriptor(
  name='HeadGroupSpec',
  full_name='flyteidl.plugins.HeadGroupSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ray_start_params', full_name='flyteidl.plugins.HeadGroupSpec.ray_start_params', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_HEADGROUPSPEC_RAYSTARTPARAMSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=299,
  serialized_end=448,
)


_WORKERGROUPSPEC_RAYSTARTPARAMSENTRY = _descriptor.Descriptor(
  name='RayStartParamsEntry',
  full_name='flyteidl.plugins.WorkerGroupSpec.RayStartParamsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='flyteidl.plugins.WorkerGroupSpec.RayStartParamsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='flyteidl.plugins.WorkerGroupSpec.RayStartParamsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=395,
  serialized_end=448,
)

_WORKERGROUPSPEC = _descriptor.Descriptor(
  name='WorkerGroupSpec',
  full_name='flyteidl.plugins.WorkerGroupSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_name', full_name='flyteidl.plugins.WorkerGroupSpec.group_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='replicas', full_name='flyteidl.plugins.WorkerGroupSpec.replicas', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_replicas', full_name='flyteidl.plugins.WorkerGroupSpec.min_replicas', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_replicas', full_name='flyteidl.plugins.WorkerGroupSpec.max_replicas', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ray_start_params', full_name='flyteidl.plugins.WorkerGroupSpec.ray_start_params', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_WORKERGROUPSPEC_RAYSTARTPARAMSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=451,
  serialized_end=686,
)

_RAYJOB.fields_by_name['ray_cluster'].message_type = _RAYCLUSTER
_RAYCLUSTER.fields_by_name['head_group_spec'].message_type = _HEADGROUPSPEC
_RAYCLUSTER.fields_by_name['worker_group_spec'].message_type = _WORKERGROUPSPEC
_HEADGROUPSPEC_RAYSTARTPARAMSENTRY.containing_type = _HEADGROUPSPEC
_HEADGROUPSPEC.fields_by_name['ray_start_params'].message_type = _HEADGROUPSPEC_RAYSTARTPARAMSENTRY
_WORKERGROUPSPEC_RAYSTARTPARAMSENTRY.containing_type = _WORKERGROUPSPEC
_WORKERGROUPSPEC.fields_by_name['ray_start_params'].message_type = _WORKERGROUPSPEC_RAYSTARTPARAMSENTRY
DESCRIPTOR.message_types_by_name['RayJob'] = _RAYJOB
DESCRIPTOR.message_types_by_name['RayCluster'] = _RAYCLUSTER
DESCRIPTOR.message_types_by_name['HeadGroupSpec'] = _HEADGROUPSPEC
DESCRIPTOR.message_types_by_name['WorkerGroupSpec'] = _WORKERGROUPSPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RayJob = _reflection.GeneratedProtocolMessageType('RayJob', (_message.Message,), dict(
  DESCRIPTOR = _RAYJOB,
  __module__ = 'flyteidl.plugins.ray_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.RayJob)
  ))
_sym_db.RegisterMessage(RayJob)

RayCluster = _reflection.GeneratedProtocolMessageType('RayCluster', (_message.Message,), dict(
  DESCRIPTOR = _RAYCLUSTER,
  __module__ = 'flyteidl.plugins.ray_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.RayCluster)
  ))
_sym_db.RegisterMessage(RayCluster)

HeadGroupSpec = _reflection.GeneratedProtocolMessageType('HeadGroupSpec', (_message.Message,), dict(

  RayStartParamsEntry = _reflection.GeneratedProtocolMessageType('RayStartParamsEntry', (_message.Message,), dict(
    DESCRIPTOR = _HEADGROUPSPEC_RAYSTARTPARAMSENTRY,
    __module__ = 'flyteidl.plugins.ray_pb2'
    # @@protoc_insertion_point(class_scope:flyteidl.plugins.HeadGroupSpec.RayStartParamsEntry)
    ))
  ,
  DESCRIPTOR = _HEADGROUPSPEC,
  __module__ = 'flyteidl.plugins.ray_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.HeadGroupSpec)
  ))
_sym_db.RegisterMessage(HeadGroupSpec)
_sym_db.RegisterMessage(HeadGroupSpec.RayStartParamsEntry)

WorkerGroupSpec = _reflection.GeneratedProtocolMessageType('WorkerGroupSpec', (_message.Message,), dict(

  RayStartParamsEntry = _reflection.GeneratedProtocolMessageType('RayStartParamsEntry', (_message.Message,), dict(
    DESCRIPTOR = _WORKERGROUPSPEC_RAYSTARTPARAMSENTRY,
    __module__ = 'flyteidl.plugins.ray_pb2'
    # @@protoc_insertion_point(class_scope:flyteidl.plugins.WorkerGroupSpec.RayStartParamsEntry)
    ))
  ,
  DESCRIPTOR = _WORKERGROUPSPEC,
  __module__ = 'flyteidl.plugins.ray_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.WorkerGroupSpec)
  ))
_sym_db.RegisterMessage(WorkerGroupSpec)
_sym_db.RegisterMessage(WorkerGroupSpec.RayStartParamsEntry)


DESCRIPTOR._options = None
_HEADGROUPSPEC_RAYSTARTPARAMSENTRY._options = None
_WORKERGROUPSPEC_RAYSTARTPARAMSENTRY._options = None
# @@protoc_insertion_point(module_scope)
