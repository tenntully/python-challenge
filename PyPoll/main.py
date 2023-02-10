'''
    PYPOLL Main Code
    GT Boot Camp - Data Vizualization
    HW3 - Python Challenge
    Jason Hanlin

    For resources: python-challenge/PyPoll/Resources

'''

import os   #import os module
import csv  #import csv module

#  Read File in python-challenge/Resources/election_data.csv
csvFilePath = os.path.join("Resources", "election_data.csv")

# Use with open command and csv.reader to read file
with open(csvFilePath, 'r') as dataFile:
    csvReader = csv.reader(dataFile, delimiter=',')
    header = next(csvReader)    #Store header as seperate variable
    data = list(csvReader)      #create a full list of all data without header

#create a condidate list for each occurance of a new candidate using set() function  
third_column = [row[2] for row in data]
candidateSet = set(third_column)
candidateList = list(candidateSet)

votesList = []         #create an empty list to add votes for each candidate
percentList = []                 #create an empty list to add percentage of votes for each candidate

totalVotes = int(len(data))   #calculate total votes 

#calculate number of votes for each candidate and make two lists with votes and percent of votes
for x in candidateList:
    VoteCounter = 0
    for ballotID, county, candidate in data:
        if candidate == x:
            VoteCounter = VoteCounter + 1

    votesList.append(VoteCounter)

    percentResults = VoteCounter/totalVotes
    percentList.append('{:,.3%}'.format(percentResults))

#Create a summary array (zip) of lists.  
#This must be called each time because otherwise it resets the zip when it is used.
#To set it up use lambda: and need to call it with () after summaryList()
summaryList = lambda: zip(candidateList, votesList, percentList)

#Calculate the winner.  No winner if nobody gets votes
winningVotes = 0  #set index for winning number of votes
for candidate, votes, percentage in summaryList():
    if votes > winningVotes: 
        winningVotes = votes
        winner = candidate
    elif winningVotes == 0:
        winner = 'No Winner'

# print results
print()
print('Election Results\n')
print('------------------------------------\n')
print('Total Votes:', totalVotes, '\n')
print('------------------------------------\n')
for candidate, votes, percentage in summaryList():
    print(f'{candidate}:    {percentage} ({votes})')    
print()
print('------------------------------------\n')
print("Winner: ", winner, '\n')
print('------------------------------------\n')

# Write ouput to the file anlysis/outputfile.txt
outputfilepath = os.path.join("analysis","outputfile.txt")

# Use with open command to write information to a file
with open(outputfilepath,'w') as txtOutput:
    txtOutput.write('')
    txtOutput.write('Election Results\n\n')
    txtOutput.write('------------------------------------\n\n')
    txtOutput.write(f'Total Votes: {totalVotes}\n\n')
    txtOutput.write('------------------------------------\n\n')
    for candidate, votes, percentage in summaryList():
        txtOutput.write(f'{candidate}:    {percentage} ({votes})\n')
    txtOutput.write('\n')
    txtOutput.write('------------------------------------\n\n')
    txtOutput.write(f'Winner: {winner}\n\n')
    txtOutput.write('------------------------------------\n\n')
 

