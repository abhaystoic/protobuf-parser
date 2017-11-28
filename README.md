# protobuf-parser
Protocol buffers are Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data – think XML, but smaller, faster, and simpler. You define how you want your data to be structured once, then you can use special generated source code to easily write and read your structured data to and from a variety of data streams and using a variety of languages.
  [https://developers.google.com/protocol-buffers/]

Google Protobuf can get complicated when there is extreme nesting in the data. This is a generic python library for parsing protobuf and extract meaningful structured information from it.

Frequently developers will be storing data based on the protobuf in different databases. One major use case of this  library then will be to generate SQL queries out of these nested protobuf.
