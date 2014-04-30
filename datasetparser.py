import csv

def getTransactions(returnPart,rows):
	"""Returns the transactions dictionary 

    Data structure: [{TID(flexible type):itemset(frozenset)}, ...]

    Args:
    	returnPart: if True returns part of the transactions, specified by rows
    	rows: ignored if returnPart is False
    """
	return _getTransactions(False,returnPart,rows)

def _getTransactions(DEBUG,returnPart,rows):
	pass
	"""Set the dataset here"""	
	csvFile = open('test2.csv', "rb", 0)
	f = csv.reader(csvFile, delimiter=',')

	transactions = []

	counter=0
	for row in f:
		if counter==0:
			pass
		else:
			"""Set the fileds to process here, specified by range() or []
			note that range(i,j) = [i, ... , j-1]
			"""
			nonNullFields=[row[i] for i in range(0,1)+[1,2] if (row[i]!='' and row[i]!='N/A')]
			transactions.append({counter:frozenset(nonNullFields)})
		counter=counter+1

	if DEBUG:
		for i in range(0,rows):
			print( transactions[i] )
		print ("The length is " + str(len(transactions))) 

	if returnPart:
		return transactions[:rows]
	else:
		return transactions

if __name__ == "__main__":
	_getTransactions(True,True,20)