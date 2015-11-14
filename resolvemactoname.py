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
    hostname = item.get('hostname')
    if key == sys.argv[1]:
        print hostname
        sys.exit(0)
