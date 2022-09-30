try:
    def voting():
        name = []
        vote = []
        s = str(input("Do you wish to vote. Enter yes or no: "))

        while(s.lower() == "yes"):
            n = str(input("Enter your name: "))
            v = int(input("Enter who you wish to vote, Candidate 1 or Candidate 2? Enter 1 or 2: "))
            name.append(n)
            vote.append(v)
            s = str(input("Do you wish to vote. Enter yes or no: "))

        print("NAME : VOTE")
        for i in range(len(name)):
            print(str(name[i]) + " : " + str(vote[i]))

        count_1 = count_2 = 0
        for x in vote:
            if(x == 1):
                count_1 = count_1 + 1
            elif(x == 2):
                count_2 = count_2 + 1
            else:
                continue

        if(count_1 > count_2):
            print("Candidate 1 won the election by " + str(count_1 - count_2) + " votes")
        elif(count_1 < count_2):
            print("Candidate 2 won the election by " + str(count_2 - count_1) + " votes")
        else:
            print("The election was a draw")
    voting()

except ValueError:
    print("Enter the vote in number")

except:
    print("Enter properly")