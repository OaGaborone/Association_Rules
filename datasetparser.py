import csv

def getTransactions(returnPart,rows):
	"""Returns the transactions dictionary 

    Data structure: [{TID(flexible type):itemset(frozenset)}, ...]

    Args:
    	returnPart: if True returns part of the transactions, specified by rows
    	rows: ignored if returnPart is False
    """
	return generateTransactions(False,returnPart,rows)

def generateTransactions(DEBUG,returnPart,rows):
	pass
	csvFile = open('311-Dataset.csv', "rb", 0)
	f = csv.reader(csvFile, delimiter=',')

	transactions = []

	counter=0
	for i in f:
		if counter==0:
			pass
		elif i[8] != '' and i[8] != 'N/A':
			transactions.append({counter:frozenset([ i[8],i[5],i[0] ])})
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
	generateTransactions(True,True,20)