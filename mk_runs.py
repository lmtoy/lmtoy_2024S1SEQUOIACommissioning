#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024S1SEQUOIACommissioning"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['MonR2'] = [ 110407 ]
on['O-Cet'] = [ 110399 ]       # this is "bench3" of the pipeline

on['O-Cet'] = [ 110399, 110401, -110403 ]  # test hack



#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['MonR2']   = ""
pars1['O-Cet'] = "qagrade=1"

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2['MonR2']   = "srdp=1 admit=0"
pars2['O-Cet'] = "bank=0 qagrade=2"

pars3 = {}
pars3['O-Cet'] = "bank=1 qagrade=3"


if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
