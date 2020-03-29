# import modules
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

Khan_vote=0
Correy_vote=0
Li_vote=0
Tooley_vote=0
total_vote=0


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        total_vote += 1
    
        if (row[2] == "Khan"):
            Khan_vote += 1
        elif (row[2] == "Correy"):
            Correy_vote += 1
        elif (row[2] == "Li"):
            Li_vote += 1
        else:
            Tooley_vote += 1
    
    # Calculate the percentage
    Khan_percent=Khan_vote/total_vote
    Correy_percent=Correy_vote/total_vote
    Li_percent=Li_vote/total_vote
    Tooley_percent=Tooley_vote/total_vote
    
    #Find the winner
    winner=max(Khan_vote, Correy_vote, Li_vote, Tooley_vote)
    
    if winner==Khan_vote:
        w_name="Khan"
    elif winner==Correy_vote:
        w_name="Correy"
    elif winner==Li_vote:
        w_name="Li"
    else:
        w_name="O'Tooley"

print("Election Results")
print(f"Total Votes:{total_vote}")
print(f"Khan:{Khan_percent*100} ({Khan_vote})")
print(f"Correy:{Correy_percent*100} ({Correy_vote})")
print(f"Li:{Li_percent*100} ({Li_vote})")
print(f"O'Tooley:{Tooley_percent*100} ({Tooley_vote})")
print(f"Winner: {w_name}")
