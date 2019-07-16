#!/usr/bin/env python3
import ais
import collections
ship_e = collections.namedtuple("ship_e","mmsi name")

ships=[]
with ais.io.open('20190715ais.dat') as aisfile:
    for msg in aisfile:
        if 'decoded' in msg and 'name' in msg['decoded']:
            s=ship_e(msg['decoded']['mmsi'],msg['decoded']['name'])
            if s not in ships:
                ships.append(s)
print("Got. {} Unique names".format(len(ships)))
ships.sort()
for vessel in ships:
    print("{} {}".format(vessel.mmsi, vessel.name))
