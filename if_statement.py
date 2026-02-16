# a=int(input("Enter the number:"))
# if a%2==0:
#     print(a, "Even Number")
# else:
#     print(a, "not Even Number")
a=eval(input("Input your number"))
if a>100:
    print("Input the valid Number Under the 100 ")
elif a>= 85:
    print("Your result is A+ Grade")
elif a>= 65 < 85:
    print("Your result is A Grade")
elif a>=55 < 65:
    print("Your result is B Grade")
elif a>=35 <55:
    print("Your result is C Grade")
elif a <0:
    print("Enter the positive number")
else:
    print("You are Fail, Try Again")