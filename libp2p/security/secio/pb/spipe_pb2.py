# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: libp2p/security/secio/pb/spipe.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='libp2p/security/secio/pb/spipe.proto',
  package='spipe.pb',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n$libp2p/security/secio/pb/spipe.proto\x12\x08spipe.pb\"_\n\x07Propose\x12\x0c\n\x04rand\x18\x01 \x01(\x0c\x12\x12\n\npublic_key\x18\x02 \x01(\x0c\x12\x11\n\texchanges\x18\x03 \x01(\t\x12\x0f\n\x07\x63iphers\x18\x04 \x01(\t\x12\x0e\n\x06hashes\x18\x05 \x01(\t\";\n\x08\x45xchange\x12\x1c\n\x14\x65phemeral_public_key\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c')
)




_PROPOSE = _descriptor.Descriptor(
  name='Propose',
  full_name='spipe.pb.Propose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rand', full_name='spipe.pb.Propose.rand', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='public_key', full_name='spipe.pb.Propose.public_key', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exchanges', full_name='spipe.pb.Propose.exchanges', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ciphers', full_name='spipe.pb.Propose.ciphers', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hashes', full_name='spipe.pb.Propose.hashes', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=145,
)


_EXCHANGE = _descriptor.Descriptor(
  name='Exchange',
  full_name='spipe.pb.Exchange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ephemeral_public_key', full_name='spipe.pb.Exchange.ephemeral_public_key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='spipe.pb.Exchange.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=147,
  serialized_end=206,
)

DESCRIPTOR.message_types_by_name['Propose'] = _PROPOSE
DESCRIPTOR.message_types_by_name['Exchange'] = _EXCHANGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Propose = _reflection.GeneratedProtocolMessageType('Propose', (_message.Message,), {
  'DESCRIPTOR' : _PROPOSE,
  '__module__' : 'libp2p.security.secio.pb.spipe_pb2'
  # @@protoc_insertion_point(class_scope:spipe.pb.Propose)
  })
_sym_db.RegisterMessage(Propose)

Exchange = _reflection.GeneratedProtocolMessageType('Exchange', (_message.Message,), {
  'DESCRIPTOR' : _EXCHANGE,
  '__module__' : 'libp2p.security.secio.pb.spipe_pb2'
  # @@protoc_insertion_point(class_scope:spipe.pb.Exchange)
  })
_sym_db.RegisterMessage(Exchange)


# @@protoc_insertion_point(module_scope)