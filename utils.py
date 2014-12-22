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


kivadir = '../data/'
 
LoansFilePaths = glob.glob(kivadir+"loans/*.json")
LendersFilePaths = glob.glob(kivadir+"lenders/*.json")

def isNonEmptyList(ell):
	return (type(ell) == list) and (ell !=[])

def isNonEmptyDictionary(d):
	return (type(d) == dict) and (isNonEmptyList(d.keys()))

def randomElement(ell):
	assert isNonEmptyList(ell), "I need a non-empty list"
	
	return ell[np.random.randint(len(ell))]


def GrabRandomLoan(LoansFilePaths):
	with open(randomElement(LoansFilePaths),'r') as io:
		jf = json.load(io)

	return randomElement(jf['loans'])


def ProjectDictionary(aList,aDictionary):
	assert isNonEmptyList(aList), "the first argument must be a non-empty list"
	assert isNonEmptyDictionary(aDictionary), "the second argument must be a non-empty dictionary"

	return [aDictionary[k] for k in aList if k in aDictionary.keys()]
