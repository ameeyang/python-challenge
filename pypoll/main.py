import csv
total_votes = 0
percentage = []
votes = []
candidates = []

with open ('election_data.csv') as csvfile:
    csv.reader = csv.reader(csvfile, delimiter=',')
    
    for row in csv.reader:
        candidates == row[2]
        total_votes = total_votes + 1
    for candidates in votes:
        candidates[votes] = votes[candidates] + 1
    else:
        candidates[votes] = 1
        
    for name in votes.items():
        percentage[name] = "{0:.0%}".format(votes_ct/total_votes)
    if votes > winner_total:
        winner_total = votes
        winner = name
        candidates = (str(election_data[0])
        percentage = (votes/total_votes)*100

    print("Election Results")
    print("Total Votes" + str(total_votes))
    print("Khan:" + " " + str(round(percentage[0],3)) + "%" 
          + "("+str(votes[0])+")")
    print("Correy:" + " " + str(round(percentage[1],3)) + "%" 
          + "("+str(votes[1])+")")
    print("Li:" + " " + str(round(percentage[2],3)) + "%" 
          + "("+str(votes[2])+")")
    print("O'Tooley:" + " " + str(round(percentage[3],3)) + "%" 
          + "("+str(votes[3])+")")
    print("winner: " + winner) 


