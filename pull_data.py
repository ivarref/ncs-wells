#!/usr/bin/python
# -*- coding: utf-8 -*-
from decimal import Decimal
import datetime
import sys
import codecs
import os
from pprint import pprint


def set_output_encoding(encoding='utf-8'):
  import sys
  import codecs
  '''When piping to the terminal, python knows the encoding needed, and
     sets it automatically. But when piping to another program (for example,
     | less), python can not check the output encoding. In that case, it 
     is None. What I am doing here is to catch this situation for both 
     stdout and stderr and force the encoding'''
  current = sys.stdout.encoding
  if current is None :
    sys.stdout = codecs.getwriter(encoding)(sys.stdout)
  current = sys.stderr.encoding
  if current is None :
    sys.stderr = codecs.getwriter(encoding)(sys.stderr)

def break_on_duplicates():
  entries = []
  def stop_on_duplicates(elem):
    if elem in entries:
      import sys
      import traceback
      traceback.print_stack()
      print "ERROR. Got duplicate " + str(elem)
      sys.exit(-1)
    entries.append(elem)
  return stop_on_duplicates

def get_url(url, filename):
  import urllib2

  if not os.path.exists('cache'):
    os.makedirs('cache')

  if not os.path.isfile(filename):
    with codecs.open(filename, encoding='utf-8', mode='w') as fd:
      print "Creating cache %s for %s ..." % (filename, url)
      response = urllib2.urlopen(url)
      fd.write(response.read().decode('utf-8-sig'))
      print "Created cache %s for %s" % (filename, url)
  
  with open(filename, 'r') as fd:
    return fd.read().decode('utf-8')

def verify_and_assign(values, data):
  if data[0] != values:
    print "Failure. Expected %s, but got %s.\nCSV format must have changed!" % (values, data)
    sys.exit(-1)
  return tuple([idx for (idx, x) in enumerate(values.split(","))])

set_output_encoding()

# Goal:
# Output
# wellbore    date    discovered_oil discovered_gas discovered_oe

if not os.path.exists('data'):
  os.makedirs('data')

exploration_data = [x.strip() for x in get_url('http://factpages.npd.no/ReportServer?/FactPages/TableView/wellbore_exploration_all&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=84.208.153.159&CultureCode=en', 'cache/exploration_wells.csv').split('\n') if x.strip() != '']

(wlbWellboreName,wlbWell,wlbDrillingOperator,wlbDrillingOperatorGroup,wlbProductionLicence,wlbPurpose,wlbStatus,wlbContent,wlbWellType,wlbEntryDate,wlbCompletionDate,wlbField,wlbDrillPermit,wlbDiscovery,wlbDiscoveryWellbore,wlbBottomHoleTemperature,wlbSeismicLocation,wlbMaxInclation,wlbKellyBushElevation,wlbFinalVerticalDepth,wlbTotalDepth,wlbWaterDepth,wlbAgeAtTd,wlbFormationAtTd,wlbMainArea,wlbDrillingFacility,wlbFacilityTypeDrilling,wlbLicensingActivity,wlbMultilateral,wlbPurposePlanned,wlbEntryYear,wlbCompletionYear,wlbReclassFromWellbore,wlbReentryExplorationActivity,wlbPlotSymbol,wlbFormationWithHc1,wlbAgeWithHc1,wlbFormationWithHc2,wlbAgeWithHc2,wlbFormationWithHc3,wlbAgeWithHc3,wlbDrillingDays,wlbReentry,wlbGeodeticDatum,wlbNsDeg,wlbNsMin,wlbNsSec,wlbNsCode,wlbEwDeg,wlbEwMin,wlbEwSec,wlbEwCode,wlbNsDecDeg,wlbEwDesDeg,wlbNsUtm,wlbEwUtm,wlbUtmZone,wlbNamePart1,wlbNamePart2,wlbNamePart3,wlbNamePart4,wlbNamePart5,wlbNamePart6,wlbPressReleaseUrl,wlbFactPageUrl,wlbFactMapUrl,wlbDiskosWellboreType,wlbDiskosWellboreParent,wlbWdssQcDate,wlbNpdidWellbore,dscNpdidDiscovery,fldNpdidField,fclNpdidFacilityDrilling,wlbNpdidWellboreReclass,prlNpdidProductionLicence,wlbDiskosWellOperator,wlbDateUpdated,wlbDateUpdatedMax,datesyncNPD) = verify_and_assign("wlbWellboreName,wlbWell,wlbDrillingOperator,wlbDrillingOperatorGroup,wlbProductionLicence,wlbPurpose,wlbStatus,wlbContent,wlbWellType,wlbEntryDate,wlbCompletionDate,wlbField,wlbDrillPermit,wlbDiscovery,wlbDiscoveryWellbore,wlbBottomHoleTemperature,wlbSeismicLocation,wlbMaxInclation,wlbKellyBushElevation,wlbFinalVerticalDepth,wlbTotalDepth,wlbWaterDepth,wlbAgeAtTd,wlbFormationAtTd,wlbMainArea,wlbDrillingFacility,wlbFacilityTypeDrilling,wlbLicensingActivity,wlbMultilateral,wlbPurposePlanned,wlbEntryYear,wlbCompletionYear,wlbReclassFromWellbore,wlbReentryExplorationActivity,wlbPlotSymbol,wlbFormationWithHc1,wlbAgeWithHc1,wlbFormationWithHc2,wlbAgeWithHc2,wlbFormationWithHc3,wlbAgeWithHc3,wlbDrillingDays,wlbReentry,wlbGeodeticDatum,wlbNsDeg,wlbNsMin,wlbNsSec,wlbNsCode,wlbEwDeg,wlbEwMin,wlbEwSec,wlbEwCode,wlbNsDecDeg,wlbEwDesDeg,wlbNsUtm,wlbEwUtm,wlbUtmZone,wlbNamePart1,wlbNamePart2,wlbNamePart3,wlbNamePart4,wlbNamePart5,wlbNamePart6,wlbPressReleaseUrl,wlbFactPageUrl,wlbFactMapUrl,wlbDiskosWellboreType,wlbDiskosWellboreParent,wlbWdssQcDate,wlbNpdidWellbore,dscNpdidDiscovery,fldNpdidField,fclNpdidFacilityDrilling,wlbNpdidWellboreReclass,prlNpdidProductionLicence,wlbDiskosWellOperator,wlbDateUpdated,wlbDateUpdatedMax,datesyncNPD", exploration_data)


exploration_data = [x.split(",") for x in exploration_data[1:]]

seen_discoveries = []

disc = {}

for line in exploration_data:
  discovery = line[wlbField]
  if discovery not in disc:
    disc[discovery] = []
  entrydate = line[wlbEntryDate].split('.')
  entrydate.reverse()
  disc[discovery].append('-'.join(entrydate))

for key in disc.keys():
  if key.strip() == '':
    continue
  disc[key].sort()
  x = disc[key][0]
  print "%s => %s vs %s" % (key, x, str((disc[key])))

with codecs.open('data/data.tsv', encoding='utf-8', mode='w') as fd:
  fd.write('wellbore\tdate\tdiscovered_oil\n')
  fd.write('%s\n' % ('\t'.join(['1234', '1998-01-01', '123.0'])))
  fd.write('%s\n' % ('\t'.join(['1234', '2000-01-01', '0.0'])))
  fd.write('%s\n' % ('\t'.join(['1234', '2002-01-01', '12.0'])))
  fd.write('%s\n' % ('\t'.join(['1234', '2010-01-01', '150.0'])))
  fd.write('%s\n' % ('\t'.join(['1234', '2012-01-01', '12.0'])))

