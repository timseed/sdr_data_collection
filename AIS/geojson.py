#!/usr/bin/env python3
import ais
import json
records = []
with ais.io.open('/Users/tseed/Dev/sdr/rtl-ais/20190715ais.dat') as aisfile:
    try:
        for msg in aisfile:
            if 'decoded' in msg:
                try:
                    jd = dict(type="Feature", properties={"name": msg['decoded']['mmsi'], "mmsi": msg['decoded']['mmsi']},
                              geometry={
                                  "type": "Point",
                                  "coordinates": [msg['decoded']['x'], msg['decoded']['y']]
                              },
                              data={'speed': msg['decoded']['sog'], 'cog': msg['decoded']['cog']})
                    records.append(jd)
                except KeyError as ke:
                    pass
    except:
        pass

print(json.dumps(records))
