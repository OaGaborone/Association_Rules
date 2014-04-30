from __future__ import print_function
from datasetparser import getTransactions
from apriori import processTransactions
from pprint import pprint


minsup=0.1
minconf=0.1

if __name__ == "__main__":

	# trans=getTransactions(True,500)
	trans=getTransactions(False,0)


	processTransactions(trans,minsup,minconf)

	# log = open("./log.txt", "w")
	# print(processTransactions(trans,minsup,minconf), file = log)
