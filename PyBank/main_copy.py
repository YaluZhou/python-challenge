# import modules
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Define variables

total_months = 0
total_net = 0
monthly_change = 0
net_change_list = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    row = next(csvreader)
# Read each row of data after the header
    
    prev_net = int(row[1])
    total_months= total_months + 1
    total_net = total_net+int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    first_row = next(csvreader)

    for row in csvreader:
        total_months= total_months + 1
        total_net = total_net+int(row[1])
        monthly_change=int(row[1])-prev_net
        net_change_list.append(monthly_change)
        
        if int(row[1])>greatest_increase:
            greatest_increase=int(row[1])
            greatest_increase_month = row[0]
        if int(row[1])<greatest_decrease:
            greatest_decrease=int(row[1])
            greatest_decrease_month=row[0]

# Calculate the average change
average_change=sum(net_change_list)/len(net_change_list)

#Find the highest and lowest change

highest= max(net_change_list)
lowest=min(net_change_list)

print(f"Total Months: $ {total_months}")
print(f"Total Change: $ {total_net}")
print(f"Average Change: $ {average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month},(${highest})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month},(${lowest})")

   
 


