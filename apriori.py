# from __future__ import print_function
from itertools import combinations
from pprint import pprint

def processTransactions(transactions,minsup,minconf):
	"""Processes transactions, returns printable data structures
	
	TODO add more documentation

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
		print("Above are the surviving ones")
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
	# print inPreviousSet(frozenset(['10306', '10314']),dicts[sizeMinusOne],sizeMinusOne)
	while len(d)!=0:
		d={}
		setList = dicts[sizeMinusOne].keys()
		for setCandidate in set([k1|k2 for k1 in setList for k2 in setList if len(k1|k2)==sizeMinusOne+2]):
			# print inPreviousSet(setCandidate,dicts[sizeMinusOne],sizeMinusOne)
			if inPreviousSet(setCandidate,dicts[sizeMinusOne],sizeMinusOne):
				candidateSup = getOccurrence(setCandidate)
				# print candidateSup
				if candidateSup >= minsup * transSize:
					# print frozenset(setCandidate),candidateSup
					d[frozenset(setCandidate)]=candidateSup


		sizeMinusOne+=1
		if len(d)!=0:
			dicts.append(d)
			# print dicts[sizeMinusOne]
			print "largest item set size :", sizeMinusOne+1





	if DEBUG:
		# log = open("./log.txt", "w")
		# print(d, file = log)
		# log.close()
		pass



if __name__ == "__main__":
	_processTransactions(True,[{1:frozenset(['a','b'])}],0.3,0.3)




