#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import pandas as pd
import numpy as np
import math
import sys

if __name__=="__main__":
    pd.options.display.max_rows = 5
    resources = pd.read_csv('raw_resources.csv')
    resources.sort_values('dscName')
    print(resources.dscName)

    #reserves = pd.read_csv('raw_reserves.csv')
    #reserves.sort('fldName')
    #print(reserves.fldName)

    frame = pd.read_csv('raw_wells.csv')
    frame = frame[pd.notnull(frame.wlbEntryDate)]
    frame = frame[frame.wlbPurpose == 'WILDCAT']
    keep_columns = ['wlbField', 'wlbDiscovery', 'wlbEntryDate', 'wlbWellboreName', 'dscNpdidDiscovery']
    pd.DataFrame({'columns': pd.Series(frame.columns.values)}).to_csv('raw_wells_columns.csv', index=False)
    
    perfect = frame
    for col in frame.columns:
        p = perfect[pd.notnull(frame[col])]
        if len(p) == 0:
            continue
        else:
            perfect = p
    perfect.to_csv('raw_wells_perfect.csv', index=False)

    for col in frame.columns:
        if col in keep_columns:
            continue
        else:
            del frame[col]
    frame = frame[pd.notnull(frame.wlbDiscovery)]
    frame.sort_values('wlbEntryDate')
    frame.to_csv('temp_discoveries.csv', index=False)
    print(frame)

    #print("hello world!")
