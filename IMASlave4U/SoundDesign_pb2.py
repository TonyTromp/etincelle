# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: IMASlave4U/SoundDesign.proto

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
  name='IMASlave4U/SoundDesign.proto',
  package='Devialet.IMASlave4U',
  syntax='proto2',
  serialized_pb=_b('\n\x1cIMASlave4U/SoundDesign.proto\x12\x13\x44\x65vialet.IMASlave4U\x1a\x1d\x43\x61llMeMaybe/CallMeMaybe.proto2a\n\x0bSoundDesign\x1aR\x92MO\n/com.devialet.twerkit.sounddesign-0.imaslave4u-0\x12\x1c\x44\x65vialet.TwerkIt.SoundDesignB\x03\x90\x01\x01')
  ,
  dependencies=[CallMeMaybe_dot_CallMeMaybe__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\220\001\001'))

_SOUNDDESIGN = _descriptor.ServiceDescriptor(
  name='SoundDesign',
  full_name='Devialet.IMASlave4U.SoundDesign',
  file=DESCRIPTOR,
  index=0,
  options=_descriptor._ParseOptions(descriptor_pb2.ServiceOptions(), _b('\222MO\n/com.devialet.twerkit.sounddesign-0.imaslave4u-0\022\034Devialet.TwerkIt.SoundDesign')),
  serialized_start=84,
  serialized_end=181,
  methods=[
])

SoundDesign = service_reflection.GeneratedServiceType('SoundDesign', (_service.Service,), dict(
  DESCRIPTOR = _SOUNDDESIGN,
  __module__ = 'IMASlave4U.SoundDesign_pb2'
  ))

SoundDesign_Stub = service_reflection.GeneratedServiceStubType('SoundDesign_Stub', (SoundDesign,), dict(
  DESCRIPTOR = _SOUNDDESIGN,
  __module__ = 'IMASlave4U.SoundDesign_pb2'
  ))


# @@protoc_insertion_point(module_scope)
