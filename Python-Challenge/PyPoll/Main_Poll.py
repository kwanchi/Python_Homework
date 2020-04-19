# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import csv

candidates = []

Khan = int(0)
Correy = int(0)
Li = int(0)
OTooley = int(0)
Other = int(0)
Total = int(0)
Total_Check = Khan + Correy + Li + OTooley + Other

Khan_Pct = Khan / Total
Correy_Pct = Correy / Total
Li_Pct = Li / Total
O_Pct = OTooley / Total

Check = Total_Check - Total    


csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath, 'r', newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
     #skip header
    next(csvfile)
    
    for row in csvfile: 
        Total +=1      
        row = row.split(",")
        pick = row[2]
          
        if pick == "Khan":
            Khan+=1
        elif pick == "Correy":
            Correy +=1
        elif pick == "O'Tooley":
            OTooley +=1
        elif pick == "Li":
            Li +=1
        else:
            Other +=1
        
print("Election Results")
print("Total Votes: " + Total)
print("Khan: " + "{:.2%}".format(Khan_Pct))
print("Correy: " + "{:.2%}".format(Correy_Pct))
print("Li: " + "{:.2%}".format(Li_Pct))
print("O'Tooley': " +  "{:.2%}".format(O_Pct))
#%%
output_path = os.path.join("..","PyPoll","py_poll_results.csv")
with open(output_path, 'w') as csvfile:
 
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Votes', 'Khan Percentage', 'Correy Percentage', "O'Tooley Percentage", "Li Percentage", "Winner"])
    
#%%    
    # Write the second row
    results = [Total, Khan_Pct, Correy_Pct, O_Pct, Li_Pct, "?"]
    csvwriter.writerow(results)

