import os
import csv

#data storage
pollData = {"Ballot ID":[], "County":[], "Candidate": []}
ballotId = []
county = []
candidate = []
totalVotes = 0
candidates = []
charlesVotes = 0
dianaVotes = 0
raymonVotes = 0
winner = ""
charlesVotesPercent = ""
dianaVotesPercent = ""
raymonVotesPercent = ""


#gets the data from the election_data.csv file and opens the file
pollPath = os.path.join('Resources/election_data.csv')
with open(pollPath) as pollFile: 
    pollReader = csv.reader(pollFile,delimiter=',')
    pollHeader = next(pollReader)
#adds pollReader info to lists for access without opening bankPath
    for row in pollReader:
        ballotId.append(int(row[0]))
        county.append(row[1])
        candidate.append(row[2])
         
#add list data to pollData dictionary
pollData["Ballot ID"] = ballotId
pollData["County"] = county
pollData["Candidate"] = candidate

#get total votes
totalVotes = len(pollData["Ballot ID"])

#get list of candidates
sortedCandidate = sorted(candidate) #sorts candidate list so the lower if statement doesn't return multiple of the same result
candidates.append(sortedCandidate[0]) #adds first candidate to candidates list becuase lower if statement misses the first one
for x in range(len(sortedCandidate)-1):
    if sortedCandidate[x] != sortedCandidate[x+1]:
        candidates.append(sortedCandidate[x+1])

#get total votes for each candidate
for x in range(len(pollData["Candidate"])):
    if pollData["Candidate"][x] == candidates[0]:
        charlesVotes += 1
    elif pollData["Candidate"][x] == candidates[1]:
        dianaVotes += 1
    elif pollData["Candidate"][x] == candidates[2]:
        raymonVotes += 1

#get the winner
if raymonVotes > dianaVotes and raymonVotes > charlesVotes:
    winner = candidates[2]
elif charlesVotes > dianaVotes and charlesVotes > raymonVotes:
    winner = candidates[0]
elif dianaVotes > charlesVotes and dianaVotes > raymonVotes:
    winner = candidates[1]

#get vote percent per candidate
charlesVotesPercent = str(round((100 *(charlesVotes / totalVotes)),3)) +"%"
dianaVotesPercent = str(round((100 *(dianaVotes / totalVotes)),3)) +"%"
raymonVotesPercent = str(round((100 *(raymonVotes / totalVotes)),3)) +"%"

#print all results
print(f"\nTotal Votes: {totalVotes}\n")
print(f"{candidates[0]}: {charlesVotesPercent}")
print(f"{candidates[1]}: {dianaVotesPercent}")
print(f"{candidates[2]}: {raymonVotesPercent}\n")
print(f"Winner: {winner}")

#create, open and write new csv file
analysis = os.path.join('analysis/poll_analysis.csv')
with open(analysis, 'w') as analysisFile:
    fileWrite = csv.writer(analysisFile, delimiter=" ")
    fileWrite.writerow(["Election"] +["Results"])
    fileWrite.writerow(["------------------------------------------"])
    fileWrite.writerow(["Total"] +["Votes:"] +[(str(totalVotes))])
    fileWrite.writerow(["------------------------------------------"])
    fileWrite.writerow(["Charles"] +["Casper"] +["Stockhame:"] +[charlesVotesPercent])
    fileWrite.writerow(["Diana"] +["DeGette:"] +[dianaVotesPercent])
    fileWrite.writerow(["Raymon"] +["Anthony"] +["Doane:"] +[raymonVotesPercent])
    fileWrite.writerow(["------------------------------------------"])
    fileWrite.writerow(["Winner:"] +[winner])