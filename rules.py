from __future__ import print_function
from datasetparser import getTransactions
from apriori import processTransactions
from pprint import pprint


"""With any min_sup >= 0.02 the program would return pretty fast."""
minsup=0.02
minconf=0.01

if __name__ == "__main__":

	# trans=getTransactions(True,2000)
	trans=getTransactions(False,0)


	processTransactions(trans,minsup,minconf)

	# log = open("./log.txt", "w")
	# print(processTransactions(trans,minsup,minconf), file = log)
