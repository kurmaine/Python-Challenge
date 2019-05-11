#HOMEWORK
# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.


# First we'll import the os module
import os

# Module for reading CSV files
import csv

bank_data = {}
values_list = []
revenue_change = []
date_relabel =[]

csvpath = os.path.join('election_data.csv')

#Creates dictionary to be used for candidate name and vote count.
poll = {}

#Sets variable, total votes, to zero for count.
total_votes = 0

with open(csvpath, newline="") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
 
    csv_header = next(csvreader)

    print(csvreader)

    mylist = list(csvreader)



for row in mylist:
    total_votes += 1
    if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
    else:
        poll[row[2]] = 1

print("Below is the total votes casted")
print(total_votes)
print("Below are the votes in relation to the candudates")
print(poll)

#create empty list for candidates and his/her vote count
candidates = []
num_votes = []

#takes dictionary keys and values and, respectively, dumps them into the lists, 
# candidates and num_votes
for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)

# creates vote percent list
vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 1))

print("Below are all the candidates who received votes.")
print(candidates)

print("Below are the percentage of votes in relation to the candidates.")
print(vote_percent)

# zips candidates, num_votes, vote_percent into tuples
clean_data = list(zip(candidates, num_votes, vote_percent))

#creates winner_list to put winners (even if there is a tie)
winner_list = []

for name in clean_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

# makes winner_list a str with the first entry
winner = winner_list[0]

#only runs if there is a tie and puts additional winners into a string separated by commas
if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]


print("The winner is... " + str(winner))