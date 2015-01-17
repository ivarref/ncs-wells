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

if not os.path.exists('data'):
  os.makedirs('data')

# On the wellbore NPD page: Table view -> Exploration -> All - long list
filename = 'cache/exploration_wells.csv'
filename = 'cache/exploration_wells_all.csv'
exploration_data = [x.strip() for x in get_url('http://factpages.npd.no/ReportServer?/FactPages/TableView/wellbore_exploration_all&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=84.208.153.159&CultureCode=en', filename).split('\n') if x.strip() != '']

(wlbWellboreName,wlbWell,wlbDrillingOperator,wlbDrillingOperatorGroup,wlbProductionLicence,wlbPurpose,wlbStatus,wlbContent,wlbWellType,wlbEntryDate,wlbCompletionDate,wlbField,wlbDrillPermit,wlbDiscovery,wlbDiscoveryWellbore,wlbBottomHoleTemperature,wlbSeismicLocation,wlbMaxInclation,wlbKellyBushElevation,wlbFinalVerticalDepth,wlbTotalDepth,wlbWaterDepth,wlbAgeAtTd,wlbFormationAtTd,wlbMainArea,wlbDrillingFacility,wlbFacilityTypeDrilling,wlbLicensingActivity,wlbMultilateral,wlbPurposePlanned,wlbEntryYear,wlbCompletionYear,wlbReclassFromWellbore,wlbReentryExplorationActivity,wlbPlotSymbol,wlbFormationWithHc1,wlbAgeWithHc1,wlbFormationWithHc2,wlbAgeWithHc2,wlbFormationWithHc3,wlbAgeWithHc3,wlbDrillingDays,wlbReentry,wlbGeodeticDatum,wlbNsDeg,wlbNsMin,wlbNsSec,wlbNsCode,wlbEwDeg,wlbEwMin,wlbEwSec,wlbEwCode,wlbNsDecDeg,wlbEwDesDeg,wlbNsUtm,wlbEwUtm,wlbUtmZone,wlbNamePart1,wlbNamePart2,wlbNamePart3,wlbNamePart4,wlbNamePart5,wlbNamePart6,wlbPressReleaseUrl,wlbFactPageUrl,wlbFactMapUrl,wlbDiskosWellboreType,wlbDiskosWellboreParent,wlbWdssQcDate,wlbNpdidWellbore,dscNpdidDiscovery,fldNpdidField,fclNpdidFacilityDrilling,wlbNpdidWellboreReclass,prlNpdidProductionLicence,wlbDiskosWellOperator,wlbDateUpdated,wlbDateUpdatedMax,datesyncNPD) = verify_and_assign("wlbWellboreName,wlbWell,wlbDrillingOperator,wlbDrillingOperatorGroup,wlbProductionLicence,wlbPurpose,wlbStatus,wlbContent,wlbWellType,wlbEntryDate,wlbCompletionDate,wlbField,wlbDrillPermit,wlbDiscovery,wlbDiscoveryWellbore,wlbBottomHoleTemperature,wlbSeismicLocation,wlbMaxInclation,wlbKellyBushElevation,wlbFinalVerticalDepth,wlbTotalDepth,wlbWaterDepth,wlbAgeAtTd,wlbFormationAtTd,wlbMainArea,wlbDrillingFacility,wlbFacilityTypeDrilling,wlbLicensingActivity,wlbMultilateral,wlbPurposePlanned,wlbEntryYear,wlbCompletionYear,wlbReclassFromWellbore,wlbReentryExplorationActivity,wlbPlotSymbol,wlbFormationWithHc1,wlbAgeWithHc1,wlbFormationWithHc2,wlbAgeWithHc2,wlbFormationWithHc3,wlbAgeWithHc3,wlbDrillingDays,wlbReentry,wlbGeodeticDatum,wlbNsDeg,wlbNsMin,wlbNsSec,wlbNsCode,wlbEwDeg,wlbEwMin,wlbEwSec,wlbEwCode,wlbNsDecDeg,wlbEwDesDeg,wlbNsUtm,wlbEwUtm,wlbUtmZone,wlbNamePart1,wlbNamePart2,wlbNamePart3,wlbNamePart4,wlbNamePart5,wlbNamePart6,wlbPressReleaseUrl,wlbFactPageUrl,wlbFactMapUrl,wlbDiskosWellboreType,wlbDiskosWellboreParent,wlbWdssQcDate,wlbNpdidWellbore,dscNpdidDiscovery,fldNpdidField,fclNpdidFacilityDrilling,wlbNpdidWellboreReclass,prlNpdidProductionLicence,wlbDiskosWellOperator,wlbDateUpdated,wlbDateUpdatedMax,datesyncNPD", exploration_data)


exploration_data = [x.split(",") for x in exploration_data[1:]]

disc = {}

# Goal:
# Output
# wellbore    date    discovered_oil    discovered_gas    discovered_oe
# cod-well1   1968..  123.0             0                 0
# cod-well2   1969..  0.0               0                 0

date_to_discoveries = {}

field_to_type = {}

for line in exploration_data:
  entrydate = line[wlbEntryDate].split('.')
  entrydate.reverse()
  iso8601_date = '-'.join(entrydate)
  if iso8601_date == '':
    # TODO 9 entries are missing this date.
    # Let's ignore it ......
    sys.stderr.write("[WARN] Skipping %s\n" % (str(line)))
    continue
  if line[wlbPurpose] != 'WILDCAT':
    continue
  field_to_type[line[wlbField]] = 'field'

  if line[wlbField] == '':
    line[wlbField] = line[wlbDiscovery]
    field_to_type[line[wlbField]] = 'discovery'

  if line[wlbField] == '':
    line[wlbField] = line[wlbWellboreName]
    field_to_type[line[wlbField]] = 'wellbore'

  discovery = line[wlbField]
  if discovery == '':
    sys.stderr.write("This shouldn't happen.\n")
    sys.exit(-1)

  if discovery not in disc:
    disc[discovery] = []
  disc[discovery].append(iso8601_date)

  if iso8601_date not in date_to_discoveries:
    date_to_discoveries[iso8601_date] = []
  date_to_discoveries[iso8601_date].append(line)

def get_resources_map():
  resources_url_csv = 'http://factpages.npd.no/ReportServer?/FactPages/TableView/discovery_reserves&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=2.150.32.28&CultureCode=en'
  resources = [x.strip() for x in get_url(resources_url_csv, 'cache/resources.csv').split("\n")]
  values = "dscName,dscReservesRC,dscRecoverableOil,dscRecoverableGas,dscRecoverableNGL,dscRecoverableCondensate,dscDateOffResEstDisplay,dscNpdidDiscovery,dscReservesDateUpdated,DatesyncNPD"
  if resources[0] != values:
    print "CSV format changed."
    sys.exit(-1)
  (dscName,dscReservesRC,dscRecoverableOil,dscRecoverableGas,dscRecoverableNGL,dscRecoverableCondensate,dscDateOffResEstDisplay,dscNpdidDiscovery,dscReservesDateUpdated,DatesyncNPD) = tuple([idx for (idx, x) in enumerate(values.split(","))])
  resources = [x.split(",") for x in resources[1:] if x.strip() != ""]
  resource_map = {}
  for res in resources:
    oil = Decimal(res[dscRecoverableOil])
    gas = Decimal(res[dscRecoverableGas])
    ngl = Decimal(res[dscRecoverableNGL])
    con = Decimal(res[dscRecoverableCondensate])
    oe = oil + gas + ngl + con
    resource_map[res[dscName]] = (oil, gas, oe)
  return resource_map

def fldname_to_reserves():
  reserves_url_csv = 'http://factpages.npd.no/ReportServer?/FactPages/TableView/field_reserves&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=84.208.160.74&CultureCode=en'
  reserves = [x.strip() for x in get_url(reserves_url_csv, 'cache/reserves.csv').split("\n") if x.strip() != ""]
  values = "fldName,fldRecoverableOil,fldRecoverableGas,fldRecoverableNGL,fldRecoverableCondensate,fldRecoverableOE,fldRemainingOil,fldRemainingGas,fldRemainingNGL,fldRemainingCondensate,fldRemainingOE,fldDateOffResEstDisplay,fldNpdidField,DatesyncNPD"
  if reserves[0] != values:
    print "CSV format changed."
    sys.exit(-1)
  (fldName,fldRecoverableOil,fldRecoverableGas,fldRecoverableNGL,fldRecoverableCondensate,fldRecoverableOE,fldRemainingOil,fldRemainingGas,fldRemainingNGL,fldRemainingCondensate,fldRemainingOE,fldDateOffResEstDisplay,fldNpdidField,DatesyncNPD) = tuple([idx for (idx, x) in enumerate("fldName,fldRecoverableOil,fldRecoverableGas,fldRecoverableNGL,fldRecoverableCondensate,fldRecoverableOE,fldRemainingOil,fldRemainingGas,fldRemainingNGL,fldRemainingCondensate,fldRemainingOE,fldDateOffResEstDisplay,fldNpdidField,DatesyncNPD".split(","))])
  reserves = [x.split(",") for x in reserves[1:] if x.strip() != ""]
  reserves_map = {}
  for reserve in reserves:
    oil = Decimal(reserve[fldRecoverableOil])
    gas = Decimal(reserve[fldRecoverableGas])
    ngl = Decimal(reserve[fldRecoverableNGL])
    con = Decimal(reserve[fldRecoverableCondensate])
    oe = oil + gas + ngl + con
    reserves_map[reserve[fldName]] = (oil, gas, oe)
  return reserves_map

def lookup_resources():
  resources = get_resources_map()
  reserves = fldname_to_reserves()
  def lookup(discovery):
    if discovery in resources:
      return resources[discovery]
    elif discovery in reserves:
      return reserves[discovery]
    else:
      print "NOT FOUND '%s'" % (discovery)
      return (Decimal(0), Decimal(0), Decimal(0))
  return lookup

lookup_field = lookup_resources()

sys.stderr.write("*** Done initial parsing ...\n")

dates = date_to_discoveries.keys()
dates.sort()

resources_map = get_resources_map()
total_oe = Decimal(0)
total_oil = Decimal(0)

with codecs.open('data/data.tsv', encoding='utf-8', mode='w') as fd:
  fd.write('wellbore\tdate\tdiscovered_oil\tdiscovered_gas\tdiscovered_oe\n')

  for date in dates:
    wells_for_date = date_to_discoveries[date]
    for line in wells_for_date:
      discovery = line[wlbField]
      reserves = { 'oil' : Decimal(0) }
      if disc[discovery][0] == date:
        (oil, gas, oe) = lookup_field(discovery)
        total_oe += oe
        total_oil += oil
        fd.write("%s\n" % ("\t".join([discovery, date, "%.2f" % (oil), "%.2f" % (gas), "%.2f" % (oe)])))
      else:
        fd.write("%s\n" % ("\t".join([discovery, date, "0", "0", "0"])))
        pass

print total_oe * Decimal(6.29) / Decimal(1000.0)
print total_oil * Decimal(6.29) / Decimal(1000.0)
      
#with codecs.open('data/data.tsv', encoding='utf-8', mode='w') as fd:
#fd.write('wellbore\tdate\tdiscovered_oil\n')
#fd.write('%s\n' % ('\t'.join(['1234', '1998-01-01', '123.0'])))
#fd.write('%s\n' % ('\t'.join(['1234', '2000-01-01', '0.0'])))
#fd.write('%s\n' % ('\t'.join(['1234', '2002-01-01', '12.0'])))
#fd.write('%s\n' % ('\t'.join(['1234', '2010-01-01', '150.0'])))
#fd.write('%s\n' % ('\t'.join(['1234', '2012-01-01', '12.0'])))



