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
from dateutil.parser import parse

kivadir = '../data/'
 
LoansFilePaths = glob.glob(kivadir+"loans/*.json")
LendersFilePaths = glob.glob(kivadir+"lenders/*.json")


LoanHeader = ['id','posted_date','loan_amount','sector','activity','funded_date','location']


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

	row = []
	for k in aList: 
		if k in aDictionary.keys():
			if k == 'location':
				if 'country' in aDictionary['location'].keys():
					row.append(aDictionary[k]['country'])
				else:
					row.append(None)
			else:
				row.append(aDictionary[k])
		else:
			row.append(None)
	return row


def RandomLoansDataFrame(N=1000):
	return pd.DataFrame([ ProjectDictionary(LoanHeader,GrabRandomLoan(LoansFilePaths) ) for k in xrange(N)],columns=LoanHeader)


def CleanLoans(df):
	df = df[df.posted_date.apply(type) != type(None)]
	df['posted_date'] = df.posted_date.apply(parse)

	return df
