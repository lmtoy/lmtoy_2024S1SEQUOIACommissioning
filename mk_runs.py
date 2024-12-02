#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024S1SEQUOIACommissioning"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on['O-Cet'] = [ 110399 ]       # this is "bench3" of the pipeline
on['O-Cet'] = [ 110399, 110401, -110403 ]  # test hack
on['MonR2']  = [ 110407 ]        # 110411 and 110405 are bad

on['mars']   = [ 120021, 120023, 121196, 121197, 121198, 121199, 121200,
	         121201, 121203, 121205, 121207, 121209, 121211, 121213,
	         121348, 121350, 121352, 121354, 121356, 121358, 121360,
	         121362, 121364, 121366, ]

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['O-Cet']  = "qagrade=1"
pars1['MonR2']  = "extent=500 dv=20 dw=40 vlsr=10 b_order=1"
pars1['mars']   = "goal=Cont"



#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2['O-Cet']   = "bank=0 qagrade=2"
pars2['MonR2']   = "bank=0 pix_list=-11,13"

pars3 = {}
pars3['O-Cet']   = "bank=1 qagrade=3"
pars3['MonR2']   = "bank=1 pix_list=-0,1,2,3,4,6,11,13"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)


