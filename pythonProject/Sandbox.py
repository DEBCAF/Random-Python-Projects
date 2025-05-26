# Andrew Wong - School Elections
# This program record and count the number of votes for candidates in school council
# Variable initialisation
pupilNames = []
candNames = ["John","Megan","Hayden","Eunice"]
pupilVotes = []
perVotes = []
schoolSize = 5
abstain = 0
# Subroutine
def countingVotes():
    global same
    numVotes = [0, 0, 0, 0]
    abstain = 0
    # For loop to get the votes of whole school
    for i in range(schoolSize):
        # Displaying a menue for the users
        print("Enter a choice to vote for each candidate:")
        print("0 : Abstain")
        for i in range(len(candNames)):
            print(i+1,":",candNames[i])
        choice = 5
        # Validation of choice
        while choice < 0 or choice > 4:
            choice = int(input("Enter your choice: "))
        pupilVotes.append(choice)
        # Selection to find which choice has been made
        if choice == 0:
            abstain += 1
        elif choice == 1:
            numVotes[0] += 1
        elif choice == 2:
            numVotes[1] += 1
        elif choice == 3:
            numVotes[2] += 1
        elif choice == 4:
            numVotes[3] += 1
    # Calculating the number of actual votes
    votes = schoolSize - abstain
    # Displaying the data for each candidate
    for i in range(len(numVotes)):
        percent = (numVotes[i]/votes)*100
        print("Candidate",i+1,candNames[i])
        print("Number of votes:",numVotes[i])
        print("Percentage of votes:",percent)
    print("There were",votes,"votes cast")
    print("There were",abstain,"people who abstained")
    # Finding if there is a tie
    sortedVotes = numVotes
    numVotes = sorted(sortedVotes)
    same = False
    three = False
    four = False
    first = -1
    second = -1
    third = -1
    fourth = -1
    for i in range(len(numVotes)-1):
        if sortedVotes[i] == sortedVotes[i+1] and not same and sortedVotes[i+1] != 0:
            same = True
            first = sortedVotes[i]
            second = sortedVotes[i+1]
        elif sortedVotes[i] == sortedVotes[i+1] and not three and sortedVotes[i+1] != 0:
            third = sortedVotes[i+1]
            three = True
        elif sortedVotes[i] == sortedVotes[i+1] and not four and sortedVotes[i+1] != 0:
            fourth = sortedVotes[i+1]
            four = True
        else:
            same = False
    if same:
        for i in range(len(numVotes)):
            if numVotes[i] == first:
                first = i
            if numVotes[i] == second:
                second = i
            if numVotes[i] == third:
                third = i
            if numVotes[i] == fourth:
                fourth = i
        for i in range(len(numVotes)):
            if i != first and i != second:
                candNames.pop(i)
# Actual program
same = True
while same:
    countingVotes()