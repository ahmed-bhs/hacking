#!/usr/bin/python2.7
import re

data = open('flag.jpg', 'rb').read()

def findndx(str, data):
    return [m.start() for m in re.finditer(str, data)]

ext = {
    '.gif': 'GIF89a',
    '.png': '\x89PNG',
    '.jpg': '\xFF\xD8\xFF\xE0',
    '.bmp': 'BM',
    '.zip': '\x50\x4B\x03\x04',
    '.7z': '\x37\x7A\xBC\xAF\27\1C'
}

for ext, pat in ext.iteritems():
    for n in findndx(pat, data):
        open('out.' + str(n) + ext, 'wb').write(data[n:])
