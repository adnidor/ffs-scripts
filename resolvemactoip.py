#!/usr/bin/python
import sys
import urllib2
import json

if len(sys.argv) < 2:
    print "argument required"
    sys.exit(1)

data = urllib2.urlopen("http://karte.freifunk-stuttgart.de/json/alfred-json-map.json")

s = json.load(data)

nodes = {}

for (key, item) in s.items():
    addrs = item.get('network').get('addresses')
    for i in addrs:
        if i.startswith('fd21'):
            addr = i
    if key == sys.argv[1]:
        print addr
        sys.exit(0)
