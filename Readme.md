# JSON Reader

This plugin reads JSON files. JSON syntax is described at http://json.org. The input file must
consist of a single valid JSON value. Typically this value will be an `array`, an `object`, or a
`string`. If the first member of a top-level `array` is an object, it will be interpreted as
metadata and the second member (if present) will be returned by the reader as content. Non-object
first members of any top-level `array` will be returned as content. In both cases, subsequent top-
level `array` members will be ignored. A top-level `object` will be interpreted as metadata, and a
value of any other type will be returned as content. If a top-level `object` contains a "content"
member, that member value will be used for content.

## Basic example

The following JSON data:

```json
[ { "title": "Basic Example"
  , "template": "base"
  }
, "This is some content."
]
```

would produce this html output:


