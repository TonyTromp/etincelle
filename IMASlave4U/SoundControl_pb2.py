# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: IMASlave4U/SoundControl.proto

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
  name='IMASlave4U/SoundControl.proto',
  package='Devialet.IMASlave4U',
  syntax='proto2',
  serialized_pb=_b('\n\x1dIMASlave4U/SoundControl.proto\x12\x13\x44\x65vialet.IMASlave4U\x1a\x1d\x43\x61llMeMaybe/CallMeMaybe.proto2\xa0\x01\n\x0cSoundControl\x1a\x8f\x01\x92M\x8b\x01\n&com.devialet.imaslave4u.soundcontrol-0\"a\n.\n!Devialet.CallMeMaybe.BoolProperty\x12\tnightMode\n/\n#Devialet.CallMeMaybe.DoubleProperty\x12\x06volume(\x00\x42\x03\x90\x01\x01')
  ,
  dependencies=[CallMeMaybe_dot_CallMeMaybe__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\220\001\001'))

_SOUNDCONTROL = _descriptor.ServiceDescriptor(
  name='SoundControl',
  full_name='Devialet.IMASlave4U.SoundControl',
  file=DESCRIPTOR,
  index=0,
  options=_descriptor._ParseOptions(descriptor_pb2.ServiceOptions(), _b('\222M\213\001\n&com.devialet.imaslave4u.soundcontrol-0\"a\n.\n!Devialet.CallMeMaybe.BoolProperty\022\tnightMode\n/\n#Devialet.CallMeMaybe.DoubleProperty\022\006volume(\000')),
  serialized_start=86,
  serialized_end=246,
  methods=[
])

SoundControl = service_reflection.GeneratedServiceType('SoundControl', (_service.Service,), dict(
  DESCRIPTOR = _SOUNDCONTROL,
  __module__ = 'IMASlave4U.SoundControl_pb2'
  ))

SoundControl_Stub = service_reflection.GeneratedServiceStubType('SoundControl_Stub', (SoundControl,), dict(
  DESCRIPTOR = _SOUNDCONTROL,
  __module__ = 'IMASlave4U.SoundControl_pb2'
  ))


# @@protoc_insertion_point(module_scope)
