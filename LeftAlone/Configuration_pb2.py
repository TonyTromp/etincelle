# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LeftAlone/Configuration.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from CallMeMaybe import CallMeMaybe_pb2 as CallMeMaybe_dot_CallMeMaybe__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='LeftAlone/Configuration.proto',
  package='Devialet.LeftAlone',
  syntax='proto2',
  serialized_pb=_b('\n\x1dLeftAlone/Configuration.proto\x12\x12\x44\x65vialet.LeftAlone\x1a\x1d\x43\x61llMeMaybe/CallMeMaybe.proto\"\t\n\x07\x46\x61keMsg2n\n\rConfiguration\x1a]\x92MZ\n(com.devialet.leftalone-0.configuration-0\".\n,\n!Devialet.CallMeMaybe.BoolProperty\x12\x07\x65nabledB\x03\x90\x01\x01')
  ,
  dependencies=[CallMeMaybe_dot_CallMeMaybe__pb2.DESCRIPTOR,])




_FAKEMSG = _descriptor.Descriptor(
  name='FakeMsg',
  full_name='Devialet.LeftAlone.FakeMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=93,
)

DESCRIPTOR.message_types_by_name['FakeMsg'] = _FAKEMSG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FakeMsg = _reflection.GeneratedProtocolMessageType('FakeMsg', (_message.Message,), dict(
  DESCRIPTOR = _FAKEMSG,
  __module__ = 'LeftAlone.Configuration_pb2'
  # @@protoc_insertion_point(class_scope:Devialet.LeftAlone.FakeMsg)
  ))
_sym_db.RegisterMessage(FakeMsg)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\220\001\001'))

_CONFIGURATION = _descriptor.ServiceDescriptor(
  name='Configuration',
  full_name='Devialet.LeftAlone.Configuration',
  file=DESCRIPTOR,
  index=0,
  options=_descriptor._ParseOptions(descriptor_pb2.ServiceOptions(), _b('\222MZ\n(com.devialet.leftalone-0.configuration-0\".\n,\n!Devialet.CallMeMaybe.BoolProperty\022\007enabled')),
  serialized_start=95,
  serialized_end=205,
  methods=[
])

Configuration = service_reflection.GeneratedServiceType('Configuration', (_service.Service,), dict(
  DESCRIPTOR = _CONFIGURATION,
  __module__ = 'LeftAlone.Configuration_pb2'
  ))

Configuration_Stub = service_reflection.GeneratedServiceStubType('Configuration_Stub', (Configuration,), dict(
  DESCRIPTOR = _CONFIGURATION,
  __module__ = 'LeftAlone.Configuration_pb2'
  ))


# @@protoc_insertion_point(module_scope)
