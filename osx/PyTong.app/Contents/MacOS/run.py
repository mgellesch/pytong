#!/usr/bin/env python

import os, sys

# the script expects the first command line parameter as the first argument,
# while OS X passes an identifier
sys.argv.pop(1)

# The script, with full path
scpt = sys.argv[0]

# Change to the Resources directory
os.chdir(os.path.dirname(scpt))
os.chdir('../Resources')

# Run the main script
execfile('gui.py')
