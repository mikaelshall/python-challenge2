# Import Modules/Dependencies 
import os 
import csv 

#Files to load 

infile = os.path.join('/Users/mikaelshall/Desktop/unc-peace-data-pt-08-2020-u-c/02-Homework/02-Python/Instructions/PyPoll/Resources/election_data.csv')

# Declare the variables
totalVotes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0
maxVotes = 0

# Read the CSV and convert it into a list of dicitonaries 
with open(infile, newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')

    csv_header = next(rows)

    for row in rows:
        # print(row[2])
        totalVotes += 1

        if row[2] == "Khan":
            Khan_votes += 1
        elif row[2] == "Correy":
            Correy_votes += 1
        elif row[2] == "Li":
            Li_votes += 1
        elif row[2] == "O'Tooley":
            OTooley_votes += 1

# Find winner
for candidate, votes in dict_candidates_and_votes.items():
    if votes > maxVotes:
        maxVotes = votes
        winner = candidate

# Dictionary_of_candidates = {
#     Khan_Votes: "Khan",
#     Correy_Votes: "Correy",
#     Li_Votes: "Li",
#     OTooley_Votes: "O'Tooley"
# }

# winner = max(Khan_Votes, Correy_Votes, Li_Votes, OTooley_Votes)

#Khan_Percent = (Khan_votes / totalVotes) * 100

print(totalVotes)
print(Khan_votes)
print(Khan_Percent)
print(winner)

# Display results
output = f"""
Election Results
-----------------------------
Total Votes: {totalVotes}
-----------------------------
Khan: {(Khan_votes/totalVotes)*100:.3f}%  ({Khan_votes:,})
Correy: {(Correy_votes/totalVotes)*100:.3f}%  ({Correy_votes:,})
Li: {(Li_votes/totalVotes)*100:.3f}%  ({Li_votes})
O'Tooley: {(OTooley_votes/totalVotes)*100:.3f}%  ({OTooley_votes:,})
------------------------------
Winner: {winner}
------------------------------
"""

print(output)