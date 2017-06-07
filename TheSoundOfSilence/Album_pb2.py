# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TheSoundOfSilence/Album.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from TheSoundOfSilence import Node_pb2 as TheSoundOfSilence_dot_Node__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='TheSoundOfSilence/Album.proto',
  package='Devialet.AudioSource',
  syntax='proto2',
  serialized_pb=_b('\n\x1dTheSoundOfSilence/Album.proto\x12\x14\x44\x65vialet.AudioSource\x1a\x1cTheSoundOfSilence/Node.proto\"|\n\x05\x41lbum\x12+\n\x07\x61rtists\x18\x01 \x03(\x0b\x32\x1a.Devialet.AudioSource.Node\x12\x0c\n\x04name\x18\x02 \x02(\t\x12*\n\x06tracks\x18\x03 \x02(\x0b\x32\x1a.Devialet.AudioSource.Node\x12\x0c\n\x04year\x18\x04 \x02(\rB\x03\x90\x01\x01')
  ,
  dependencies=[TheSoundOfSilence_dot_Node__pb2.DESCRIPTOR,])




_ALBUM = _descriptor.Descriptor(
  name='Album',
  full_name='Devialet.AudioSource.Album',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='artists', full_name='Devialet.AudioSource.Album.artists', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Devialet.AudioSource.Album.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tracks', full_name='Devialet.AudioSource.Album.tracks', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='year', full_name='Devialet.AudioSource.Album.year', index=3,
      number=4, type=13, cpp_type=3, label=2,
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
  serialized_start=85,
  serialized_end=209,
)

_ALBUM.fields_by_name['artists'].message_type = TheSoundOfSilence_dot_Node__pb2._NODE
_ALBUM.fields_by_name['tracks'].message_type = TheSoundOfSilence_dot_Node__pb2._NODE
DESCRIPTOR.message_types_by_name['Album'] = _ALBUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Album = _reflection.GeneratedProtocolMessageType('Album', (_message.Message,), dict(
  DESCRIPTOR = _ALBUM,
  __module__ = 'TheSoundOfSilence.Album_pb2'
  # @@protoc_insertion_point(class_scope:Devialet.AudioSource.Album)
  ))
_sym_db.RegisterMessage(Album)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\220\001\001'))
# @@protoc_insertion_point(module_scope)
