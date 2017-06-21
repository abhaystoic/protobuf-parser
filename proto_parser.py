import addressbook_pb2

_desc = addressbook_pb2.DESCRIPTOR

class ProtoParser:
  """Class for parsing protos"""
  def __init__(self):
    self.columns = []

  def decide_and_prepare(self, key, value):
    for k in value.fields_by_name.values():
      if k.type != 11:
        self.columns.append(k.full_name)
      else:
        self.parse_proto(value, 'nested')

  def parse_proto(self, desc, type='normal'):
    if type == 'normal':
      for key, value in desc.message_types_by_name.items():
        self.decide_and_prepare(key, value)
    else:
      for key, value in desc.nested_types_by_name.items():
        self.decide_and_prepare(key, value)

if __name__ == "__main__":
  parserObj = ProtoParser()
  parserObj.parse_proto(_desc)
  return parserObj.columns