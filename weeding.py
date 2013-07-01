#built off of the work of others! Heavily influenced by http://stackoverflow.com/questions/11584528/iteratively-copy-specific-rows-from-csv-file-to-new-file
#weeding.py was initially written to help me sort through my collection at Hampshire College and figure out what I needed to weed based on circulation stats. Since the lists are not outrageously large, I do go through the new file and determine if I REALLY want to weed that item or not. 
#Note: the lists I worked with were never extremely large (no more than 2500 items, so far) so I can't speak to the effectiveness of the code on larger files.
#Please do contact me if you have any questions! Thea Atwood; @librarianThea on Twitter

import csv
from collections import OrderedDict

#this will appropriately order the field names for display in the final docment
ordered_fieldnames=OrderedDict([('Primary Call No Desc',None),('Last Loan Date',None),('Publication Date', None), ('total_loans', None), ('Bib Doc Number', None), ('Title', None),('Description', None),('HAM SYS #', None), ('Number of Bib records in FC', None),('1', None),('2', None),('3', None), ('4', None),('5', None),('6',None)])


#opens the appropriate file
f = open('C:\Users\Thea Atwood\Documents\Projects\Weeding\Hamp_BF_FC_duplicates_MASTER.txt', "rb") #change the file path as appropriate plz
reader = csv.DictReader(f, delimiter='\t', fieldnames=ordered_fieldnames) #dictReader for tab delimited files
writer = open('output.txt', "wb") 
writer = csv.DictWriter(writer, delimiter='\t', fieldnames=ordered_fieldnames) #going to write as a tab delimited file
writer.writeheader() #writes the headers on the new document


#iterating over the appropriate weeding parameters - extend & narrow as necessary
for row in reader:
    if row['total_loans'] == '5':
      writer.writerow(row)
    elif row['total_loans'] == '4':
	    writer.writerow(row)
    elif row['total_loans'] == '3':
	    writer.writerow(row)
    elif row['total_loans'] == '2':
        writer.writerow(row)
    elif row['total_loans'] == '1':
        writer.writerow(row)
    elif row['total_loans'] == '0':
        writer.writerow(row)
