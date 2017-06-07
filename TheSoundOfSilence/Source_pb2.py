# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TheSoundOfSilence/Source.proto

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


from CallMeMaybe import CommonMessages_pb2 as CallMeMaybe_dot_CommonMessages__pb2
from TheSoundOfSilence import Session_pb2 as TheSoundOfSilence_dot_Session__pb2
from TheSoundOfSilence import Picture_pb2 as TheSoundOfSilence_dot_Picture__pb2
from CallMeMaybe import CallMeMaybe_pb2 as CallMeMaybe_dot_CallMeMaybe__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='TheSoundOfSilence/Source.proto',
  package='Devialet.AudioSource',
  syntax='proto2',
  serialized_pb=_b('\n\x1eTheSoundOfSilence/Source.proto\x12\x14\x44\x65vialet.AudioSource\x1a CallMeMaybe/CommonMessages.proto\x1a\x1fTheSoundOfSilence/Session.proto\x1a\x1fTheSoundOfSilence/Picture.proto\x1a\x1d\x43\x61llMeMaybe/CallMeMaybe.proto\"h\n\x0bSourceError\"Y\n\x04\x43ode\x12\x11\n\rInternalError\x10\x01\x12\x10\n\x0cNotSupported\x10\x02\x12\x14\n\x10PermissionDenied\x10\x03\x12\x16\n\x12ObjectNotAvailable\x10\x04\"\x18\n\x07\x45nabled\x12\r\n\x05value\x18\x01 \x02(\x08\"\x10\n\x02Id\x12\n\n\x02id\x18\x01 \x02(\x0c\"\x12\n\x03Uri\x12\x0b\n\x03uri\x18\x01 \x02(\t2\xcd\x01\n\rSourceSession\x12<\n\x03uri\x12\x18.Devialet.AudioSource.Id\x1a\x19.Devialet.AudioSource.Uri\"\x00\x1a~\x92M{\n\x1d\x63om.devialet.source-session-0\x1a%Devialet.AudioSource.SourceError.Code\"3\n1\n#Devialet.CallMeMaybe.StringProperty\x12\x08sourceId \x01\x32\xdc\x01\n\x0f\x43onfigureSource\x12J\n\nsetEnabled\x12\x1d.Devialet.AudioSource.Enabled\x1a\x1b.Devialet.CallMeMaybe.Empty\"\x00\x1a}\x92Mz\n\x1f\x63om.devialet.source-configure-0\x1a%Devialet.AudioSource.SourceError.Code\"0\n.\n\"Devialet.CallMeMaybe.BytesProperty\x12\x08settings2\xb6\x05\n\x06Source\x12\x44\n\x04logo\x12\x1b.Devialet.CallMeMaybe.Empty\x1a\x1d.Devialet.AudioSource.Picture\"\x00\x12Q\n\x0csessionAdded\x12\x1d.Devialet.AudioSource.Session\x1a\x1b.Devialet.CallMeMaybe.Empty\"\x05\x92M\x02\x08\x01\x12U\n\x0esessionRemoved\x12\x1f.Devialet.AudioSource.SessionId\x1a\x1b.Devialet.CallMeMaybe.Empty\"\x05\x92M\x02\x08\x01\x12G\n\x07\x62igLogo\x12\x1b.Devialet.CallMeMaybe.Empty\x1a\x1d.Devialet.AudioSource.Picture\"\x00\x1a\xf2\x02\x92M\xee\x02\n\x15\x63om.devialet.source-0\x1a%Devialet.AudioSource.SourceError.Code\"\xad\x02\n+\n#Devialet.CallMeMaybe.StringProperty\x12\x02id \x01\n.\n!Devialet.CallMeMaybe.BoolProperty\x12\tisEnabled\n1\n!Devialet.CallMeMaybe.BoolProperty\x12\nisSeekable \x01\n5\n\x1d\x44\x65vialet.AudioSource.Sessions\x12\x12listActiveSessions \x01\n-\n#Devialet.CallMeMaybe.StringProperty\x12\x04name \x01\n5\n!Devialet.CallMeMaybe.BoolProperty\x12\x0esupportsEnable \x01\x42\x03\x90\x01\x01')
  ,
  dependencies=[CallMeMaybe_dot_CommonMessages__pb2.DESCRIPTOR,TheSoundOfSilence_dot_Session__pb2.DESCRIPTOR,TheSoundOfSilence_dot_Picture__pb2.DESCRIPTOR,CallMeMaybe_dot_CallMeMaybe__pb2.DESCRIPTOR,])



_SOURCEERROR_CODE = _descriptor.EnumDescriptor(
  name='Code',
  full_name='Devialet.AudioSource.SourceError.Code',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='InternalError', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NotSupported', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PermissionDenied', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ObjectNotAvailable', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=202,
  serialized_end=291,
)
_sym_db.RegisterEnumDescriptor(_SOURCEERROR_CODE)


_SOURCEERROR = _descriptor.Descriptor(
  name='SourceError',
  full_name='Devialet.AudioSource.SourceError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SOURCEERROR_CODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=187,
  serialized_end=291,
)


_ENABLED = _descriptor.Descriptor(
  name='Enabled',
  full_name='Devialet.AudioSource.Enabled',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Devialet.AudioSource.Enabled.value', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=293,
  serialized_end=317,
)


_ID = _descriptor.Descriptor(
  name='Id',
  full_name='Devialet.AudioSource.Id',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Devialet.AudioSource.Id.id', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=319,
  serialized_end=335,
)


_URI = _descriptor.Descriptor(
  name='Uri',
  full_name='Devialet.AudioSource.Uri',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uri', full_name='Devialet.AudioSource.Uri.uri', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=337,
  serialized_end=355,
)

_SOURCEERROR_CODE.containing_type = _SOURCEERROR
DESCRIPTOR.message_types_by_name['SourceError'] = _SOURCEERROR
DESCRIPTOR.message_types_by_name['Enabled'] = _ENABLED
DESCRIPTOR.message_types_by_name['Id'] = _ID
DESCRIPTOR.message_types_by_name['Uri'] = _URI
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SourceError = _reflection.GeneratedProtocolMessageType('SourceError', (_message.Message,), dict(
  DESCRIPTOR = _SOURCEERROR,
  __module__ = 'TheSoundOfSilence.Source_pb2'
  # @@protoc_insertion_point(class_scope:Devialet.AudioSource.SourceError)
  ))
_sym_db.RegisterMessage(SourceError)

Enabled = _reflection.GeneratedProtocolMessageType('Enabled', (_message.Message,), dict(
  DESCRIPTOR = _ENABLED,
  __module__ = 'TheSoundOfSilence.Source_pb2'
  # @@protoc_insertion_point(class_scope:Devialet.AudioSource.Enabled)
  ))
_sym_db.RegisterMessage(Enabled)

Id = _reflection.GeneratedProtocolMessageType('Id', (_message.Message,), dict(
  DESCRIPTOR = _ID,
  __module__ = 'TheSoundOfSilence.Source_pb2'
  # @@protoc_insertion_point(class_scope:Devialet.AudioSource.Id)
  ))
_sym_db.RegisterMessage(Id)

Uri = _reflection.GeneratedProtocolMessageType('Uri', (_message.Message,), dict(
  DESCRIPTOR = _URI,
  __module__ = 'TheSoundOfSilence.Source_pb2'
  # @@protoc_insertion_point(class_scope:Devialet.AudioSource.Uri)
  ))
_sym_db.RegisterMessage(Uri)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\220\001\001'))

_SOURCESESSION = _descriptor.ServiceDescriptor(
  name='SourceSession',
  full_name='Devialet.AudioSource.SourceSession',
  file=DESCRIPTOR,
  index=0,
  options=_descriptor._ParseOptions(descriptor_pb2.ServiceOptions(), _b('\222M{\n\035com.devialet.source-session-0\032%Devialet.AudioSource.SourceError.Code\"3\n1\n#Devialet.CallMeMaybe.StringProperty\022\010sourceId \001')),
  serialized_start=358,
  serialized_end=563,
  methods=[
  _descriptor.MethodDescriptor(
    name='uri',
    full_name='Devialet.AudioSource.SourceSession.uri',
    index=0,
    containing_service=None,
    input_type=_ID,
    output_type=_URI,
    options=None,
  ),
])

SourceSession = service_reflection.GeneratedServiceType('SourceSession', (_service.Service,), dict(
  DESCRIPTOR = _SOURCESESSION,
  __module__ = 'TheSoundOfSilence.Source_pb2'
  ))

SourceSession_Stub = service_reflection.GeneratedServiceStubType('SourceSession_Stub', (SourceSession,), dict(
  DESCRIPTOR = _SOURCESESSION,
  __module__ = 'TheSoundOfSilence.Source_pb2'
  ))



_CONFIGURESOURCE = _descriptor.ServiceDescriptor(
  name='ConfigureSource',
  full_name='Devialet.AudioSource.ConfigureSource',
  file=DESCRIPTOR,
  index=1,
  options=_descriptor._ParseOptions(descriptor_pb2.ServiceOptions(), _b('\222Mz\n\037com.devialet.source-configure-0\032%Devialet.AudioSource.SourceError.Code\"0\n.\n\"Devialet.CallMeMaybe.BytesProperty\022\010settings')),
  serialized_start=566,
  serialized_end=786,
  methods=[
  _descriptor.MethodDescriptor(
    name='setEnabled',
    full_name='Devialet.AudioSource.ConfigureSource.setEnabled',
    index=0,
    containing_service=None,
    input_type=_ENABLED,
    output_type=CallMeMaybe_dot_CommonMessages__pb2._EMPTY,
    options=None,
  ),
])

ConfigureSource = service_reflection.GeneratedServiceType('ConfigureSource', (_service.Service,), dict(
  DESCRIPTOR = _CONFIGURESOURCE,
  __module__ = 'TheSoundOfSilence.Source_pb2'
  ))

ConfigureSource_Stub = service_reflection.GeneratedServiceStubType('ConfigureSource_Stub', (ConfigureSource,), dict(
  DESCRIPTOR = _CONFIGURESOURCE,
  __module__ = 'TheSoundOfSilence.Source_pb2'
  ))



_SOURCE = _descriptor.ServiceDescriptor(
  name='Source',
  full_name='Devialet.AudioSource.Source',
  file=DESCRIPTOR,
  index=2,
  options=_descriptor._ParseOptions(descriptor_pb2.ServiceOptions(), _b('\222M\356\002\n\025com.devialet.source-0\032%Devialet.AudioSource.SourceError.Code\"\255\002\n+\n#Devialet.CallMeMaybe.StringProperty\022\002id \001\n.\n!Devialet.CallMeMaybe.BoolProperty\022\tisEnabled\n1\n!Devialet.CallMeMaybe.BoolProperty\022\nisSeekable \001\n5\n\035Devialet.AudioSource.Sessions\022\022listActiveSessions \001\n-\n#Devialet.CallMeMaybe.StringProperty\022\004name \001\n5\n!Devialet.CallMeMaybe.BoolProperty\022\016supportsEnable \001')),
  serialized_start=789,
  serialized_end=1483,
  methods=[
  _descriptor.MethodDescriptor(
    name='logo',
    full_name='Devialet.AudioSource.Source.logo',
    index=0,
    containing_service=None,
    input_type=CallMeMaybe_dot_CommonMessages__pb2._EMPTY,
    output_type=TheSoundOfSilence_dot_Picture__pb2._PICTURE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='sessionAdded',
    full_name='Devialet.AudioSource.Source.sessionAdded',
    index=1,
    containing_service=None,
    input_type=TheSoundOfSilence_dot_Session__pb2._SESSION,
    output_type=CallMeMaybe_dot_CommonMessages__pb2._EMPTY,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\222M\002\010\001')),
  ),
  _descriptor.MethodDescriptor(
    name='sessionRemoved',
    full_name='Devialet.AudioSource.Source.sessionRemoved',
    index=2,
    containing_service=None,
    input_type=TheSoundOfSilence_dot_Session__pb2._SESSIONID,
    output_type=CallMeMaybe_dot_CommonMessages__pb2._EMPTY,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\222M\002\010\001')),
  ),
  _descriptor.MethodDescriptor(
    name='bigLogo',
    full_name='Devialet.AudioSource.Source.bigLogo',
    index=3,
    containing_service=None,
    input_type=CallMeMaybe_dot_CommonMessages__pb2._EMPTY,
    output_type=TheSoundOfSilence_dot_Picture__pb2._PICTURE,
    options=None,
  ),
])

Source = service_reflection.GeneratedServiceType('Source', (_service.Service,), dict(
  DESCRIPTOR = _SOURCE,
  __module__ = 'TheSoundOfSilence.Source_pb2'
  ))

Source_Stub = service_reflection.GeneratedServiceStubType('Source_Stub', (Source,), dict(
  DESCRIPTOR = _SOURCE,
  __module__ = 'TheSoundOfSilence.Source_pb2'
  ))


# @@protoc_insertion_point(module_scope)
