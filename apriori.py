from pprint import pprint

def processTransaction(transactions):
	"""Processes transactions, returns printable data structures
	TODO add more documentation
	"""
	return _processTransaction(False,transactions)	

def _processTransaction(DEBUG,transactions):

	if DEBUG:
		pprint(transactions)


if __name__ == "__main__":
	_processTransaction(True,None)