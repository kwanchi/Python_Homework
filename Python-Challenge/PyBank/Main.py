# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import csv

total_months = 0
total_volume = 0
total_change = 0
most_gain = {"date":"", "amount":0}
most_loss = {"date":"", "amount":0}
Row = 0
currentrow = None
previousrow = None

csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath, 'r', newline = "") as csvfile:
    #skip header
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvfile)
    
    for row in csvfile: 
        
        total_months +=1
        row = row.split(",")
        total_volume +=int(row[1])
        
       # print(total_months, net_total)
       #set value of previous row for the first iteration, so you can start computing the difference from 2nd iteration on: 
        if previousrow is None:
            previousrow = row
            continue
        #the above accounts for the first subtraction, now we can resume to i=2 on out:
        currentrow = row
        change = int(currentrow[1]) - int(previousrow[1])
        total_change += change
        if change < 0 and change < most_loss["amount"]:
            #fill in the most_loss!
            most_loss["amount"] = change
            most_loss["date"] = currentrow[0]
        elif change > 0 and change > most_gain["amount"]:
                most_gain["amount"] = change
                most_gain["date"] = currentrow[0]
        previousrow = row
        
avg_change = str(round(total_change / (total_months - 1), 2))
#avg_change_str = str(round(avg_change, 2))
total_volume_with_comma = "{:,}".format(total_volume)                                

print("Total Months: " + str(total_months)) 
print("Total : $" + total_volume_with_comma) 
print("Average Change:" + avg_change)
print("Greatest Increase in Proits: " + str(most_gain["date"]) + " $" + str(most_gain["amount"]))
print("Greatest Decrease in Proits: " + str(most_loss["date"]) + " $" + str(most_loss["amount"]))
    
output_path = os.path.join("..","PyBank","py_bank_results.csv")
with open(output_path, 'w') as csvfile:
 
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Months', 'Total Volume', 'Average Monthly Change', 'Greatest Increase Date','Greatest Decrease'])
    
    
    # Write the second row
    results = [total_months,total_volume_with_comma,avg_change,most_gain["amount"], most_loss["amount"]]
    csvwriter.writerow(results)
    
     
      
'''
create a Python script that analyzes the records to calculate each of the following:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The average of the changes in "Profit/Losses" over the entire period

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in losses (date and amount) over the entire period

As an example, your analysis should look similar to the one below:

Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
In addition, your final script should both print the 
analysis to the terminal and export a text file with the results.
'''
