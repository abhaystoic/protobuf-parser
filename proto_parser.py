"""This module provides a very simple proto parser."""
from sample import addressbook_pb2

class ProtoParser:
  """Class for parsing protos"""

  def __init__(self):
    self.columns = []

  def _decide_and_prepare(self, message_type):
    """Decides whether the proto message is nested or simple.

    Args:
      message_type: Message type object.
    """
    for k in message_type.fields_by_name.values():
      if k.type != 11:
        self.columns.append(k.full_name)
      else:
        self._parse_proto(message_type, 'nested')

  def _parse_proto(self, desc, type='normal'):
    if type == 'normal':
      for key, message_type in desc.message_types_by_name.items():
        self._decide_and_prepare(message_type)
    else:
      for key, message_type in desc.nested_types_by_name.items():
        self._decide_and_prepare(message_type)

  def parse(self, desc):
    self._parse_proto(desc)
    return self.columns

if __name__ == "__main__":
  """This can be considered as a test for now."""
  parserObj = ProtoParser()
  print parserObj.parse(addressbook_pb2.DESCRIPTOR)