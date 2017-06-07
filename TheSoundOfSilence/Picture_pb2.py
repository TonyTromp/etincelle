# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TheSoundOfSilence/Picture.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from CallMeMaybe import CallMeMaybe_pb2 as CallMeMaybe_dot_CallMeMaybe__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='TheSoundOfSilence/Picture.proto',
  package='Devialet.AudioSource',
  syntax='proto2',
  serialized_pb=_b('\n\x1fTheSoundOfSilence/Picture.proto\x12\x14\x44\x65vialet.AudioSource\x1a\x1d\x43\x61llMeMaybe/CallMeMaybe.proto\"\x7f\n\x07Picture\x12\x0c\n\x04size\x18\x01 \x02(\r\x12\x0c\n\x04type\x18\x02 \x02(\r\x12\x13\n\x04\x64\x61ta\x18\x03 \x02(\x0c\x42\x05\x92M\x02\x08\x00\"(\n\x04Size\x12\t\n\x05Large\x10\x01\x12\n\n\x06Normal\x10\x02\x12\t\n\x05Small\x10\x03\"\x19\n\x04Type\x12\x08\n\x04Http\x10\x01\x12\x07\n\x03Raw\x10\x02\"\x17\n\tPictureId\x12\n\n\x02id\x18\x01 \x02(\x0c\x42\x03\x90\x01\x01')
  ,
  dependencies=[CallMeMaybe_dot_CallMeMaybe__pb2.DESCRIPTOR,])



_PICTURE_SIZE = _descriptor.EnumDescriptor(
  name='Size',
  full_name='Devialet.AudioSource.Picture.Size',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Large', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Normal', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Small', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=148,
  serialized_end=188,
)
_sym_db.RegisterEnumDescriptor(_PICTURE_SIZE)

_PICTURE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Devialet.AudioSource.Picture.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Http', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Raw', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=190,
  serialized_end=215,
)
_sym_db.RegisterEnumDescriptor(_PICTURE_TYPE)


_PICTURE = _descriptor.Descriptor(
  name='Picture',
  full_name='Devialet.AudioSource.Picture',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='Devialet.AudioSource.Picture.size', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Devialet.AudioSource.Picture.type', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='Devialet.AudioSource.Picture.data', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222M\002\010\000'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PICTURE_SIZE,
    _PICTURE_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=215,
)


_PICTUREID = _descriptor.Descriptor(
  name='PictureId',
  full_name='Devialet.AudioSource.PictureId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Devialet.AudioSource.PictureId.id', index=0,
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
  serialized_start=217,
  serialized_end=240,
)

_PICTURE_SIZE.containing_type = _PICTURE
_PICTURE_TYPE.containing_type = _PICTURE
DESCRIPTOR.message_types_by_name['Picture'] = _PICTURE
DESCRIPTOR.message_types_by_name['PictureId'] = _PICTUREID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Picture = _reflection.GeneratedProtocolMessageType('Picture', (_message.Message,), dict(
  DESCRIPTOR = _PICTURE,
  __module__ = 'TheSoundOfSilence.Picture_pb2'
  # @@protoc_insertion_point(class_scope:Devialet.AudioSource.Picture)
  ))
_sym_db.RegisterMessage(Picture)

PictureId = _reflection.GeneratedProtocolMessageType('PictureId', (_message.Message,), dict(
  DESCRIPTOR = _PICTUREID,
  __module__ = 'TheSoundOfSilence.Picture_pb2'
  # @@protoc_insertion_point(class_scope:Devialet.AudioSource.PictureId)
  ))
_sym_db.RegisterMessage(PictureId)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\220\001\001'))
_PICTURE.fields_by_name['data'].has_options = True
_PICTURE.fields_by_name['data']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222M\002\010\000'))
# @@protoc_insertion_point(module_scope)
