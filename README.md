# sdr_data_collection

This is a small repo for storing data files that I have collected from some rtl-sdr programs I have been running.


### Why do this ?

I was surprised that despite AIS/1080 data being easy to access via a web interface, there seemmed to be a lack of data files for programmers who wanted to explore this data rather than deal with the pre-processed data. 

  - All data has been collected personally by myself, and left for a couple of days prior to uploading - removing any OpSec issues regarding ship security etc. 
  - All files have data errors in them. This is what an RTL-SDR device would yield to your program. So you are expected to be able to deal with such events.
  - Geo diversity. Alas this is not good. They have all been taken from the same region - Hong Kong S.A.R.

### AIS 

There are a few data files here, and 3 example python scripts to process the data. 

  - Extract Ship Names [Extract Ship Names](./AIS/ship_name.py)
  - Create a GeoJSON output [geojson example](./AIS/geojson.py) 
  - Plot your AIS antenna receiving range [Ship position extract](./AIS/Ais Ship position extract/Ais Ship position extract.md)