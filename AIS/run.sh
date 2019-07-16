#!/bin/bash
echo "Web Access on 127.0.0.1:8899"
fn=$(date +'%Y%m%d')"ais.dat"
./rtl_ais -n -h 127.0.0.1 -P 8899 2>&1 | tee -a $fn
