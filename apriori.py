# from __future__ import print_function
from __future__ import division
from itertools import combinations
from pprint import pprint

def processTransactions(transactions,minsup,minconf):
	"""Processes transactions, returns printable data structures
	
	The results will be printed on screen directly.

	"""
	return _processTransactions(False,transactions,minsup,minconf)	

def _processTransactions(DEBUG,transactions,minsup,minconf):

	DEBUG=DEBUG

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
	# 
	# pprint(d)
			
	if DEBUG:
		pprint(d)
		print("============================")
		print("Above is all the items")
		print("============================")
		numItems = len(d.keys())

	def delLowSupItems(d):
		for dKey in d.keys():
			if d[dKey] < minsup * transSize:
				del d[dKey]
		dicts.append(d)

	delLowSupItems(d)
	# 
	# pprint(dicts[0])

	if DEBUG:
		numSurvive = len(dicts[0].keys())
		pprint(dicts[0])
		print("============================")
		print("Above is the surviving ones")
		print("============================")
		print("With min_sup of "+str(minsup)+", we have "+str(numItems)+" items, of which "+ str(numSurvive)+" survived, the # of transactions is "+str(transSize)+".")


	def getOccurrence(subSet):
		count=0
		for tran in transactions:
			for itemSet in tran.values():
				if subSet<=itemSet:
					count+=1
		return count

	def inPreviousSet(setCandidate,previousSet,sizeMinusOne):
		for subCandidate in set(combinations(setCandidate,sizeMinusOne+1)):
			if set(subCandidate) not in previousSet.keys():
				return False
		return True


	sizeMinusOne=0
	while len(d)!=0:
		d={}
		setList = dicts[sizeMinusOne].keys()
		for setCandidate in set([k1|k2 for k1 in setList for k2 in setList if len(k1|k2)==sizeMinusOne+2]):
			if inPreviousSet(setCandidate,dicts[sizeMinusOne],sizeMinusOne):
				candidateSup = getOccurrence(setCandidate)
				if candidateSup >= minsup * transSize:
					# print frozenset(setCandidate),candidateSup
					d[frozenset(setCandidate)]=candidateSup

		sizeMinusOne+=1
		if len(d)!=0:
			dicts.append(d)
	# 
	print "largest item set size :", sizeMinusOne


	rules={}
	for i in range(0,len(dicts)):
		dict_=dicts[i]
		for largeset in dict_.keys():
			dividend=dict_[largeset]
			for lSize in range(1,len(largeset)):
				for lCandidate in set(combinations(largeset,lSize)):
					conf=dividend/dicts[lSize-1][frozenset(lCandidate)]
					print dividend,dicts[lSize-1][frozenset(lCandidate)]
					if conf >= minconf:
						rules[tuple([frozenset(lCandidate),largeset-frozenset(lCandidate)])]=conf
	pprint(rules)



	# for all dicts
	# 	for each largeset in dict[i].keys()
	# 		dividend = dict[i][largeset]
	# 		for all possible length 1 to len(dict)-1
	# 			generate subsets
	# 			for each set in subsets
	# 				conf = dividend/dicts[size-1][set]
	# 				if conf>=minconf:
	# 					dconf[[set,largeset-set]]=conf






	if DEBUG:
		# log = open("./log.txt", "w")
		# print(d, file = log)
		# log.close()
		pass



if __name__ == "__main__":
	_processTransactions(True,[{1:frozenset(['a','b'])}],0.3,0.3)




