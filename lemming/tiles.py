from __future__ import division, print_function, unicode_literals
range = xrange
unzip = lambda l:apply(zip,l)

# the variables that we export:
info = {}
width = 16
height = 16

import data
f = data.load("tiles.txt")
tile_txt = f.read()
f.close()

lines = tile_txt.split("\n")
first_line = lines.pop(0)
headers = [header.split(":") for header in first_line.strip().split()]
header_names, header_types = unzip(headers)

type_str_to_func = {
    'str': lambda s: s,
    'int': int,
    'bool': lambda b: bool(int(b)),
    'float': float,
}

assert headers[0][0] == 'id'
for full_line in lines:
    line = full_line.strip()
    if line.startswith("#") or len(line) == 0:
        continue
    
    parts = line.split()
    assert len(parts) == len(header_names)

    for i, part in enumerate(parts):
        parts[i] = type_str_to_func[header_types[i]](part)

    info[parts[0]] = dict(zip(header_names, parts))
