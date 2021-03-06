# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gait_recorder_message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gait_recorder_message.proto',
  package='gait_recorder_message.msgs',
  serialized_pb='\n\x1bgait_recorder_message.proto\x12\x1agait_recorder_message.msgs\"\xeb\x01\n\x0eGaitRecMessage\x12\x11\n\tModelName\x18\x01 \x02(\t\x12\x10\n\x08NewFrame\x18\x02 \x02(\x08\x12\x12\n\nPlayStatus\x18\x03 \x02(\x08\x12\x17\n\x0bJointAngles\x18\x04 \x03(\x01\x42\x02\x10\x01\x12\r\n\x05Timer\x18\x05 \x01(\x05\x12\x11\n\tCondition\x18\x06 \x01(\t\x12\x12\n\nDependency\x18\x07 \x01(\t\x12\x10\n\x08\x45xtrInfo\x18\x08 \x01(\t\x12\x11\n\x05\x46lags\x18\t \x03(\x05\x42\x02\x10\x01\x12\x11\n\tResetFlag\x18\n \x01(\x08\x12\x19\n\x11LoadConfiguration\x18\x0b \x01(\x08')




_GAITRECMESSAGE = _descriptor.Descriptor(
  name='GaitRecMessage',
  full_name='gait_recorder_message.msgs.GaitRecMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ModelName', full_name='gait_recorder_message.msgs.GaitRecMessage.ModelName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='NewFrame', full_name='gait_recorder_message.msgs.GaitRecMessage.NewFrame', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PlayStatus', full_name='gait_recorder_message.msgs.GaitRecMessage.PlayStatus', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='JointAngles', full_name='gait_recorder_message.msgs.GaitRecMessage.JointAngles', index=3,
      number=4, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='Timer', full_name='gait_recorder_message.msgs.GaitRecMessage.Timer', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Condition', full_name='gait_recorder_message.msgs.GaitRecMessage.Condition', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Dependency', full_name='gait_recorder_message.msgs.GaitRecMessage.Dependency', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ExtrInfo', full_name='gait_recorder_message.msgs.GaitRecMessage.ExtrInfo', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Flags', full_name='gait_recorder_message.msgs.GaitRecMessage.Flags', index=8,
      number=9, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='ResetFlag', full_name='gait_recorder_message.msgs.GaitRecMessage.ResetFlag', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LoadConfiguration', full_name='gait_recorder_message.msgs.GaitRecMessage.LoadConfiguration', index=10,
      number=11, type=8, cpp_type=7, label=1,
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
  extension_ranges=[],
  serialized_start=60,
  serialized_end=295,
)

DESCRIPTOR.message_types_by_name['GaitRecMessage'] = _GAITRECMESSAGE

class GaitRecMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GAITRECMESSAGE

  # @@protoc_insertion_point(class_scope:gait_recorder_message.msgs.GaitRecMessage)


_GAITRECMESSAGE.fields_by_name['JointAngles'].has_options = True
_GAITRECMESSAGE.fields_by_name['JointAngles']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_GAITRECMESSAGE.fields_by_name['Flags'].has_options = True
_GAITRECMESSAGE.fields_by_name['Flags']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
# @@protoc_insertion_point(module_scope)
