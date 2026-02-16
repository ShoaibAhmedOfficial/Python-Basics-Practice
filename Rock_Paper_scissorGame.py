import random
l=["rock","paper","scissor"]
while True:
    Ccount=0
    Ucount=0
    uc=int(input('''
        Game Start...
        1 YES
        2 NO
    '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
                1 Rock
                2 Paper
                3 Scissor
            '''))
            if userInput==1:
                unchoice="rock"
            elif userInput==2:
                unchoice="paper"
            elif userInput==3:
                unchoice="scissor"
            Cchoice=random.choice(l)
            if Cchoice==unchoice:
                print("computer Value",Cchoice)
                print("User Value",unchoice)
                print("Game Draw")
                Ccount=Ccount+1
                Ucount=Ucount+1
            elif (Cchoice=="scissor" and unchoice=="rock") or (Cchoice=="rock" and unchoice=="paper") or (Cchoice=="paper" and unchoice=="scissor"):
                print("computer Value", Cchoice)
                print("User Value", unchoice)
                print("You Win")
                Ucount = Ucount + 1
            else:
                print("computer Value", Cchoice)
                print("User Value", unchoice)
                print("Computer Win")
                Ccount = Ccount + 1
        if Ucount==Ccount:
            print("Final Result of the Game is Draw")
            print("User Score",Ucount)
            print("Computer Score", Ccount)
        elif Ucount>Ccount:
            print("You win the Game")
            print("User Score", Ucount)
            print("Computer Score", Ccount)
        else:
            print("Computer Win the Game")
            print("User Score", Ucount)
            print("Computer Score", Ccount)
    else:
        break
