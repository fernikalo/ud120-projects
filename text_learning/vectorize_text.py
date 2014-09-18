#!/usr/bin/python

import pickle
import sys
import re
sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

""" 
    starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification

    the list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    the actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project

    the data is stored in lists and packed away in pickle files at the end

"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        path = "../"+path[:-1]
        print path
        email = open(path, "r")

        ### use parseOutText to extract the text from the opened email

        ### use str.replace() to remove any instances of the words
        ### ["sara", "shackleton", "chris", "germani"] 

        ### append the text to word_data

        ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris


    email.close()

print "emails processed"
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )





### in Part 4, do TfIdf vectorization here


