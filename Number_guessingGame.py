import random
number=random.randrange(1,11)
while True:
    User_input=int(input("Enter the number between 1 to 10:  "))

    if User_input<1 or User_input>10 :
        print("you are out off range")
    elif User_input == number:
        print("Computer NUmber",number)
        print("you Guess the right")
        break
    else:
        # print("computer Number",number)
        print("you guess the Wrong")
