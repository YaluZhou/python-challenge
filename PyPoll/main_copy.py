# import modules
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Improved Reading using CSV module

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    Khan_vote=0
    Correy_vote=0
    Li_vote=0
    Tooley_vote=0

# Read each row of data after the header
    for row in csvreader:
       length_row=sum(1 for row in csvreader)
    print(f"Total Votes: {length_row}")


# Read each candidates votes
    for row in csvreader:
       if row[2]=="Khan":
          Khan_vote=Khan_vote+1
          print(Khan_vote)
          
