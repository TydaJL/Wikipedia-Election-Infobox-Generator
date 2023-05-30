# {{Election box begin | title= Angmering & Findon}}
# {{Election box winning candidate with party link||party=Conservative Party (UK)|candidate=Deborah Urquhart|votes=1596|percentage=55.7|change=-5.8}}
# {{Election box candidate with party link||party=Liberal Democrats (UK)|candidate=Louisa Fowles|votes=754|percentage=26.3|change=+8.1}}
# {{Election box candidate with party link||party=Labour Party (UK)|candidate=Alison Baker|votes=310|percentage=10.8|change=-2.7}}
# {{Election box candidate with party link||party=Green Party of England and Wales|candidate=Chris Medland|votes=207|percentage=7.2|change=''N/A''}}
# {{Election box majority||votes=842|percentage=29.4|change=-13.9}}
# {{Election box turnout|
#  |votes = 2,867|percentage = 31.7|change =-2.8}}
# {{Election box hold with party link|
#  |winner = Conservative Party (UK)
#  |swing = }}
# {{Election box end}}

candidatesDone = False
constituencyName = input("What is the name of the Constituency?")
candidatesDict = {}
totalVotes = 0
while candidatesDone == False:
    candidateParty = input("What party is the candidate affiliated with?")
    candidateName = input("What is the candidate's name?")
    candidateVotes = int(input(f"How many votes did {candidateName} receive?"))
    totalVotes += candidateVotes
    candidatePartyPastVote = input(f"What percentage of the vote did the {candidateParty} receive in the previous election? Write N/A if this party did not contest the previous election.")
    candidatesDict[candidateParty] = {"Party": candidateParty, "Name": candidateName, "Votes": candidateVotes, "Party Previous Vote": candidatePartyPastVote}
    complete = input("Are you done filling out candidates? Enter 'Y' if complete and 'N' if incomplete.")
    if complete == "Y" or complete == "Yes":
        candidatesDone = True



generatedString = f"{{{{Election box begin | title= {constituencyName}}}}}\n"

print(generatedString)