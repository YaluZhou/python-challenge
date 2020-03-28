# import modules
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Improved Reading using CSV module

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    
# Read each row of data after the header
    for row in csvreader:
     list1=[row[1]]
     max_list=max(list1)
 
