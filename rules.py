from __future__ import print_function
from datasetparser import getTransactions
from apriori import processTransactions
from optparse import OptionParser

from pprint import pprint


"""With any min_sup >= 0.02 the program would return pretty fast."""

if __name__ == "__main__":

	optparser = OptionParser()
	optparser.add_option('-s', '--minSupport',dest='minS',help='minimum support value',default=0.02,type='float')
	optparser.add_option('-c', '--minConfidence',dest='minC',help='minimum confidence value',default=0.2,type='float')
	(options, args) = optparser.parse_args()
	minsup = options.minS
	minconf = options.minC

	# trans=getTransactions(True,2000)
	"""Use all data rows"""
	trans=getTransactions(False,0)
	processTransactions(trans,minsup,minconf)