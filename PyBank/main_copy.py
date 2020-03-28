# import modules
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Improved Reading using CSV module

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

# Read each row of data after the header
    for row in csvreader:
       length_row=sum(1 for row in csvreader)
    print(f"Total Months: {length_row}")

with open(csvpath) as csvfile:

    csvreader_total = csv.reader(csvfile, delimiter=',')
    header=next(csvreader_total)
    total=0.0
    
# Read each row of data after the header
    for row in csvreader_total:
       total +=int(row[1])
       Average=total/length_row
       
    print(f"Total: $ {float(total)}")
    print(f"Average Change: $ {Average}")
   
 


