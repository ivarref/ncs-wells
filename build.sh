#!/bin/bash

clear
./pull2.py
fswatch -e ".*" -i ".*/[^.]*\\.py$" -i ".*/[^.]*\\.sh$" -0 . | xargs -0 -n 1 -I {} /bin/sh -c 'clear; ./pull2.py'
