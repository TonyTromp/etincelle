# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TooManyFlows/Playlist.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from CallMeMaybe import CommonMessages_pb2 as CallMeMaybe_dot_CommonMessages__pb2
from CallMeMaybe import CallMeMaybe_pb2 as CallMeMaybe_dot_CallMeMaybe__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='TooManyFlows/Playlist.proto',
  package='Devialet.TooManyFlows',
  syntax='proto2',
  serialized_pb=_b('\n\x1bTooManyFlows/Playlist.proto\x12\x15\x44\x65vialet.TooManyFlows\x1a CallMeMaybe/CommonMessages.proto\x1a\x1d\x43\x61llMeMaybe/CallMeMaybe.proto\"&\n\x08TrackMsg\x12\r\n\x05index\x18\x01 \x02(\r\x12\x0b\n\x03url\x18\x02 \x02(\t\"<\n\tTracksMsg\x12/\n\x06tracks\x18\x01 \x03(\x0b\x32\x1f.Devialet.TooManyFlows.TrackMsg\"j\n\x07MoveMsg\x12.\n\x05\x66irst\x18\x01 \x02(\x0b\x32\x1f.Devialet.TooManyFlows.TrackMsg\x12/\n\x06second\x18\x02 \x02(\x0b\x32\x1f.Devialet.TooManyFlows.TrackMsg2\x94\x07\n\x08Playlist\x12\x43\n\x05\x63lear\x12\x1b.Devialet.CallMeMaybe.Empty\x1a\x1b.Devialet.CallMeMaybe.Empty\"\x00\x12I\n\x06insert\x12 .Devialet.TooManyFlows.TracksMsg\x1a\x1b.Devialet.CallMeMaybe.Empty\"\x00\x12\x45\n\x04move\x12\x1e.Devialet.TooManyFlows.MoveMsg\x1a\x1b.Devialet.CallMeMaybe.Empty\"\x00\x12I\n\x06remove\x12 .Devialet.TooManyFlows.TracksMsg\x1a\x1b.Devialet.CallMeMaybe.Empty\"\x00\x12J\n\x07\x63leared\x12\x1b.Devialet.CallMeMaybe.Empty\x1a\x1b.Devialet.CallMeMaybe.Empty\"\x05\x92M\x02\x08\x01\x12S\n\x0btracksAdded\x12 .Devialet.TooManyFlows.TracksMsg\x1a\x1b.Devialet.CallMeMaybe.Empty\"\x05\x92M\x02\x08\x01\x12P\n\ntrackMoved\x12\x1e.Devialet.TooManyFlows.MoveMsg\x1a\x1b.Devialet.CallMeMaybe.Empty\"\x05\x92M\x02\x08\x01\x12U\n\rtracksRemoved\x12 .Devialet.TooManyFlows.TracksMsg\x1a\x1b.Devialet.CallMeMaybe.Empty\"\x05\x92M\x02\x08\x01\x1a\x9b\x02\x92M\x97\x02\n$com.devialet.toomanyflows.playlist-0\"\xee\x01\n0\n\x1e\x44\x65vialet.TooManyFlows.TrackMsg\x12\x0c\x63urrentTrack\x18\x01\n0\n#Devialet.CallMeMaybe.UInt32Property\x12\x07maxSize \x01\n+\n!Devialet.CallMeMaybe.BoolProperty\x12\x06random\n.\n!Devialet.CallMeMaybe.BoolProperty\x12\trepeatAll\n+\n\x1f\x44\x65vialet.TooManyFlows.TracksMsg\x12\x06tracks \x01')
  ,
  dependencies=[CallMeMaybe_dot_CommonMessages__pb2.DESCRIPTOR,CallMeMaybe_dot_CallMeMaybe__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TRACKMSG = _descriptor.Descriptor(
  name='TrackMsg',
  full_name='Devialet.TooManyFlows.TrackMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='Devialet.TooManyFlows.TrackMsg.index', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='Devialet.TooManyFlows.TrackMsg.url', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  serialized_start=119,
  serialized_end=157,
)


_TRACKSMSG = _descriptor.Descriptor(
  name='TracksMsg',
  full_name='Devialet.TooManyFlows.TracksMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tracks', full_name='Devialet.TooManyFlows.TracksMsg.tracks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=159,
  serialized_end=219,
)


_MOVEMSG = _descriptor.Descriptor(
  name='MoveMsg',
  full_name='Devialet.TooManyFlows.MoveMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first', full_name='Devialet.TooManyFlows.MoveMsg.first', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='second', full_name='Devialet.TooManyFlows.MoveMsg.second', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=221,
  serialized_end=327,
)

_TRACKSMSG.fields_by_name['tracks'].message_type = _TRACKMSG
_MOVEMSG.fields_by_name['first'].message_type = _TRACKMSG
_MOVEMSG.fields_by_name['second'].message_type = _TRACKMSG
DESCRIPTOR.message_types_by_name['TrackMsg'] = _TRACKMSG
DESCRIPTOR.message_types_by_name['TracksMsg'] = _TRACKSMSG
DESCRIPTOR.message_types_by_name['MoveMsg'] = _MOVEMSG

TrackMsg = _reflection.GeneratedProtocolMessageType('TrackMsg', (_message.Message,), dict(
  DESCRIPTOR = _TRACKMSG,
  __module__ = 'TooManyFlows.Playlist_pb2'
  # @@protoc_insertion_point(class_scope:Devialet.TooManyFlows.TrackMsg)
  ))
_sym_db.RegisterMessage(TrackMsg)

TracksMsg = _reflection.GeneratedProtocolMessageType('TracksMsg', (_message.Message,), dict(
  DESCRIPTOR = _TRACKSMSG,
  __module__ = 'TooManyFlows.Playlist_pb2'
  # @@protoc_insertion_point(class_scope:Devialet.TooManyFlows.TracksMsg)
  ))
_sym_db.RegisterMessage(TracksMsg)

MoveMsg = _reflection.GeneratedProtocolMessageType('MoveMsg', (_message.Message,), dict(
  DESCRIPTOR = _MOVEMSG,
  __module__ = 'TooManyFlows.Playlist_pb2'
  # @@protoc_insertion_point(class_scope:Devialet.TooManyFlows.MoveMsg)
  ))
_sym_db.RegisterMessage(MoveMsg)


# @@protoc_insertion_point(module_scope)
