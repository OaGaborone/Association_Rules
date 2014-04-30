from datasetparser import getTransactions
from pprint import pprint

if __name__ == "__main__":

	trans=getTransactions(True,100)

	pprint( trans)
