import sys
import os
import glob
import string
import math
import json
import gzip
import itertools

import datetime as dt
import numpy as np
import pandas as pd

from collections import deque, Counter

SLrootDirectory = os.path.realpath('.')

def GetKiva(getnew=False):
	if getnew:
		print "Getting a new JSON Snapshot!"	
		print "I will put it above ", SLrootDirectory
		kivapath = os.path.realpath('..')+"/kiva_ds_json.zip"

		if not os.path.exists(kivapath):
			print "You don't seem to have a snapshot.  I will get one from the kiva website!"
			os.system("wget http://s3.kiva.org/snapshots/kiva_ds_json.zip --output-document="+kivapath)
		else:
			os.system("ls -lstrh "+kivapath)
	else:
		pass


GetKiva(True)
