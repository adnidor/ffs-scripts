#!/usr/bin/python
import urllib2
import json

data = urllib2.urlopen("http://karte.freifunk-stuttgart.de/json/alfred-json-map.json")

s = json.load(data)

nodes_ip = {}
nodes_mac = {}

for (key, item) in s.items():
    hostname = item.get('hostname')
    addrs = item.get('network').get('addresses')
    for i in addrs:
        if i.startswith('fd21'):
            addr = i
    host_ip = {hostname:addr}
    host_mac = {hostname:key}
    nodes_ip.update(host_ip)
    nodes_mac.update(host_mac)


whitelist = open("whitelist-macs.txt", "w")
with open("whitelist-names.txt", "r") as ins:
    for line in ins:
        if nodes_mac.has_key(line.rstrip()):
            whitelist.write(nodes_mac.get(line.rstrip())+"\n")
whitelist.close()
