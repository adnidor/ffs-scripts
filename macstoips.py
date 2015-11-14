#!/usr/bin/python
import urllib2
import json

data = urllib2.urlopen("http://karte.freifunk-stuttgart.de/json/alfred-json-map.json")

s = json.load(data)

nodes_name = {}
nodes_mac = {}

for (key, item) in s.items():
    hostname = item.get('hostname')
    addrs = item.get('network').get('addresses')
    for i in addrs:
        if i.startswith('fd21'):
            addr = i
    host_mac = {key:addr}
    host_name = {key:hostname}
    nodes_mac.update(host_mac)
    nodes_name.update(host_name)


whitelist = open("whitelist.txt", "w")
whitelist_names = open("whitelist-names.txt", "w")
with open("whitelist-macs.txt", "r") as ins:
    for line in ins:
        if nodes_mac.has_key(line.rstrip()):
            whitelist.write(nodes_mac.get(line.rstrip())+"\n")
            whitelist_names.write(nodes_name.get(line.rstrip())+"\n")
whitelist.close()
whitelist_names.close()
