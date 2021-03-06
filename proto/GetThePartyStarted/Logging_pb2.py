# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GetThePartyStarted/Logging.proto

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
from CallMeMaybe import CallMeMaybe_pb2 as CallMeMaybe_dot_CallMeMaybe__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='GetThePartyStarted/Logging.proto',
  package='Devialet.GetThePartyStarted',
  syntax='proto2',
  serialized_pb=_b('\n GetThePartyStarted/Logging.proto\x12\x1b\x44\x65vialet.GetThePartyStarted\x1a CallMeMaybe/CommonMessages.proto\x1a\x1d\x43\x61llMeMaybe/CallMeMaybe.proto\">\n\x11UploadLogsRequest\x12\x16\n\x0einstallationId\x18\x01 \x02(\t\x12\x11\n\ttimestamp\x18\x02 \x02(\x03\x32\x9f\x01\n\x0bLogUploader\x12[\n\nuploadLogs\x12..Devialet.GetThePartyStarted.UploadLogsRequest\x1a\x1b.Devialet.CallMeMaybe.Empty\"\x00\x1a\x33\x92M0\n.com.devialet.getthepartystarted.log-uploader-0B\x03\x90\x01\x01')
  ,
  dependencies=[CallMeMaybe_dot_CommonMessages__pb2.DESCRIPTOR,CallMeMaybe_dot_CallMeMaybe__pb2.DESCRIPTOR,])




_UPLOADLOGSREQUEST = _descriptor.Descriptor(
  name='UploadLogsRequest',
  full_name='Devialet.GetThePartyStarted.UploadLogsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='installationId', full_name='Devialet.GetThePartyStarted.UploadLogsRequest.installationId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Devialet.GetThePartyStarted.UploadLogsRequest.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=130,
  serialized_end=192,
)

DESCRIPTOR.message_types_by_name['UploadLogsRequest'] = _UPLOADLOGSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UploadLogsRequest = _reflection.GeneratedProtocolMessageType('UploadLogsRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPLOADLOGSREQUEST,
  __module__ = 'GetThePartyStarted.Logging_pb2'
  # @@protoc_insertion_point(class_scope:Devialet.GetThePartyStarted.UploadLogsRequest)
  ))
_sym_db.RegisterMessage(UploadLogsRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\220\001\001'))

_LOGUPLOADER = _descriptor.ServiceDescriptor(
  name='LogUploader',
  full_name='Devialet.GetThePartyStarted.LogUploader',
  file=DESCRIPTOR,
  index=0,
  options=_descriptor._ParseOptions(descriptor_pb2.ServiceOptions(), _b('\222M0\n.com.devialet.getthepartystarted.log-uploader-0')),
  serialized_start=195,
  serialized_end=354,
  methods=[
  _descriptor.MethodDescriptor(
    name='uploadLogs',
    full_name='Devialet.GetThePartyStarted.LogUploader.uploadLogs',
    index=0,
    containing_service=None,
    input_type=_UPLOADLOGSREQUEST,
    output_type=CallMeMaybe_dot_CommonMessages__pb2._EMPTY,
    options=None,
  ),
])

LogUploader = service_reflection.GeneratedServiceType('LogUploader', (_service.Service,), dict(
  DESCRIPTOR = _LOGUPLOADER,
  __module__ = 'GetThePartyStarted.Logging_pb2'
  ))

LogUploader_Stub = service_reflection.GeneratedServiceStubType('LogUploader_Stub', (LogUploader,), dict(
  DESCRIPTOR = _LOGUPLOADER,
  __module__ = 'GetThePartyStarted.Logging_pb2'
  ))


# @@protoc_insertion_point(module_scope)
