import sys
import os

# First argument should be the filename
filename = sys.argv[1]

# Based on the second argument, we can decide whether it is an infobox or a question
infobox = sys.argv[2] == "infobox"
question = sys.argv[2] == "question"

# If infobox is selected
if infobox == True:
  with open(filename) as f:
    content = f.readlines()
  for query in content:
    os.system("python infobox.py " + "'"+str(query)+"'")

# If question is selected
if question == True:
  with open(filename) as f:
    content = f.readlines()
  for query in content:
    os.system("python question.py " + "'"+str(query)+"'")      	