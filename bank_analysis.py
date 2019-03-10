# Import dependencies
import os
import csv

budget_path = os.path.join('..','HWK3','budget_data.csv')

# Read in the CSV file
with open(budget_path, newline="") as budget_csv:

    # Split the data on commas
    budget_data = csv.reader(budget_csv, delimiter=',')
    header = next(budget_data)

    # Total numbers of months included in the dataset
    row_count = sum(1 for row in budget_data)
    
    #convert file to lists
    lst = []
    for line in budget_data:
        lst.append([ int(x) for x in line.split()])
    column1 = [ x[0] for x in lst]
    column2 = [ x[1] for x in lst]

    # Net amount P&L over the entire period
    sum_PnL = sum(x for x in column2)
    
    # Net amount P&L over the entire period
    def avg_PnL(column2):
        length = len(column2)
        total = 0.0
        for x in column2:
            total += x
        return total / length

    # Print results 
    print(f"Total months = {row_count}")
    print(f"Total Profit & Losses = ${sum_PnL}")
    print(f"Average Profit & Losses = ${avg_PnL}")