from datasetparser import getTransactions
from apriori import processTransaction
from pprint import pprint

minsup=0.1
minconf=0.1

if __name__ == "__main__":

	trans=getTransactions(True,100)

	processTransaction(trans)

