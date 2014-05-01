'''
This plugin reads JSON files. JSON syntax is described at http://json.org. The input file must
consist of a single valid JSON value. Typically this value will be an array, an object, or a
string. If the first member of a top-level array is an object, it will be interpreted as
metadata and the second member (if present) will be returned by the reader as content. Non-
object first members of top-level arrays will be returned as content. In both cases, subsequent
top-level array members will be ignored. A top-level object will be interpreted as metadata,
and a value of any other type will be returned as content. If a top-level object contains a
"content" member, that member value will be used for content.
'''

import json
from pelican import signals
from pelican.readers import BaseReader
from pelican.utils import pelican_open

class JSONReader(BaseReader):
    enabled = True
    file_extensions = ('json',)

    def __init__(self, settings):
        super(JSONReader, self).__init__(settings)

    def read(self, source_path):
        content, metadata = '', {}
        try:
            with pelican_open(source_path) as text:
                obj = json.loads(text)
        except ValueError:      # if file can't be parsed, ignore it
            pass
        else:
            if isinstance(obj, list):
                try:
                    first = obj.pop(0)
                    if isinstance(first, dict):
                        metadata = first
                        content = obj.pop(0)
                    else:
                        content = first
                except IndexError:
                    pass
            elif isinstance(obj, dict):
                metadata = obj
                content = metadata.pop('content', '')
            else:               # str or number or True or False or None
                content = obj
        return content, metadata

def add_reader(readers):
    readers.reader_classes['json'] = JSONReader

def register():
    signals.readers_init.connect(add_reader)
