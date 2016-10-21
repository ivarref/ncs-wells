#!/bin/bash

set -ex

rm -fv raw_*.csv

curl "http://factpages.npd.no/ReportServer?/FactPages/TableView/wellbore_exploration_all&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=84.208.153.159&CultureCode=en" \
| awk 'NR==1{sub(/^\xef\xbb\xbf/,"")}{print}' > raw_wells.csv

curl "http://factpages.npd.no/ReportServer?/FactPages/TableView/discovery_reserves&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=84.208.153.159&CultureCode=en" \
| awk 'NR==1{sub(/^\xef\xbb\xbf/,"")}{print}' > raw_resources.csv

curl "http://factpages.npd.no/ReportServer?/FactPages/TableView/field_reserves&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=84.208.153.159&CultureCode=en" \
| awk 'NR==1{sub(/^\xef\xbb\xbf/,"")}{print}' > raw_reserves.csv
