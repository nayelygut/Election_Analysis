#Add our dependencies
import csv
import os
from typing import TYPE_CHECKING
#assign a variable for the file to load and the path
file_to_load='Resources/election_results.csv'
#assign a variable to save the file to a path
filet_to_save='analysis/election_analysis.txt'
#Total vote counter before opening the file
total_votes=0
#Candidate list
candidate_options=[]
#declare a dictionary
candidate_votes={}
#Winning candidate and winning count tracker
winning_candidate=''
winning_count= 0
winning_percentage=0
#Open the election results and read the file
with open(file_to_load) as election_data:
    #to do: read an analyze the data here
    file_reader=csv.reader(election_data)
    #Read header row
    headers=next(file_reader)
    #Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
        #Print the candidate name for each row
        candidate_name= row[2]
        #Add the candidate name to the candidate list if a candidate name does not match an existing candidate
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #Add candidate name and zero votes to the dictionary
            candidate_votes[candidate_name]=0
        #Add a vote each time the candidate name comes up
        candidate_votes[candidate_name] += 1
    #iterate through the candidate list
    for candidate_name in candidate_votes:
        #retrieve vote count for a candidate
        votes=candidate_votes[candidate_name]
        vote_percentage = (float(votes)/float(total_votes))*100
        print(f'{candidate_name}: {vote_percentage:.1F}% ({votes:,})\n')
        if votes > winning_count and vote_percentage > winning_percentage:
            winning_count = votes
            winning_percentage= vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary= (
        f'---------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'---------------------\n')
    print(winning_candidate_summary)

#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote



