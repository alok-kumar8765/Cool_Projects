nominee_1 = input("Enter the name of 1st nominee: ")
nominee_2 = input("Enter the name of 2st nominee: ")

nm1_vote = 0
nm2_vote = 0

voter_id = [1,2,3,4,5,6,7,8,9,10]

no_of_voter = len(voter_id)

while True:
    if voter_id == []:
        print('voting over')
        if nm1_vote > nm2_vote:
            percent = (nm1_vote/nm2_vote)*100
            print(nominee_1,'Has won with : ',percent)
            break
        elif nm2_vote>nm1_vote:
            percent = (nm2_vote/nm1_vote)*100
            print(nominee_2,'Has won with : ',percent)
            break
        else:
            print('tie')
            break
        
    voter = int(input('Enter your voter id : '))
    if voter in voter_id:
        print("you are a voter")
        voter_id.remove(voter)
        print("-----------------------------------")
        print("To give vote to",nominee_1,"press 1")
        print("To give vote to",nominee_2,"press 2")
        print("-----------------------------------")
        vote = int(input('Enter your vote : '))
        if vote == 1:
            nm1_vote += 1
            print(nominee_1,"thank u")
        elif vote == 2:
            nm2_vote += 1
            print(nominee_2,"thank u")
        elif vote > 2:
            print('check your pressed key')
        else:
            print('you are not voter')