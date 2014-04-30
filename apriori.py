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

	"""Generate the itemsets with 1 item"""
	d={}
	for tran in transactions:
		for itemSet in tran.values():
			for item in itemSet:
				if frozenset([item]) in d:
					d[frozenset([item])]+=1
				else:
					d[frozenset([item])]=1
	
	pprint(d)
	print("============================")
	print("Above is all the items")
	print("============================")

	numItems = len(d.keys())

	for dKey in d.keys():
		if d[dKey] < minsup * transSize:
			del d[dKey]
	dicts.append(d)

	numSurvive = len(dicts[0].keys())

	pprint(dicts[0])
	print("============================")
	print("Above are the surviving ones")
	print("============================")

	print("With min_sup of "+str(minsup)+", we have "+str(numItems)+" items, of which "+ str(numSurvive)+" survived, the # of transactions is "+str(transSize)+".")




	if DEBUG:
		# log = open("./log.txt", "w")
		# print(d, file = log)
		# log.close()
		pass



if __name__ == "__main__":
	_processTransactions(True,None,0.3,0.3)




