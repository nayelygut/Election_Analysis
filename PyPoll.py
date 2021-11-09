#Add our dependencies
import csv
import os
#assign a variable for the file to load and the path
file_to_load='Resources/election_results.csv'
#assign a variable to save the file to a path
filet_to_save='analysis/election_analysis.txt'
#Open the election results and read the file
with open(file_to_load) as election_data:
    #to do: read an analyze the data here
    file_reader=csv.reader(election_data)
    #Print each row in the CSV file
    #for row in file_reader:
    headers=next(file_reader)
    print(headers)

#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote



