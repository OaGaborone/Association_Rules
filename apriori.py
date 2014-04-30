# from __future__ import print_function
from pprint import pprint

def processTransactions(transactions,minsup,minconf):
	"""Processes transactions, returns printable data structures
	
	TODO add more documentation

	"""
	return _processTransactions(False,transactions,minsup,minconf)	

def _processTransactions(DEBUG,transactions,minsup,minconf):

	transSize = len(transactions)
	dicts=[]
	d={}
	for tran in transactions:
		for itemSet in tran.values():
			for item in itemSet:
				# print item
				if frozenset([item]) in d:
					d[frozenset([item])]+=1
				else:
					d[frozenset([item])]=1

	dicts.append(d)
	
	# log = open("./log.txt", "w")
	# print(d, file = log)
	# log.close()

	pprint(dicts[0])




	if DEBUG:
		pprint(transactions)








if __name__ == "__main__":
	_processTransactions(True,None,0.3,0.3)