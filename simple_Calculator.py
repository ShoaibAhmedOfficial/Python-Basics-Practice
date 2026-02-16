print("Enter only three value:")
a=int(input("enter the number1: "))
b=int(input("enter the number2: "))
c=int(input("enter the number3: "))
opr=input("Enter the opr")
if opr=="+":
    print(a+b+c)
elif opr=="-":
    print(a-b-c)
elif opr=="*":
    print(a*b*c)
elif opr=="/":
    print(a/b/c)
else:
    print("invalid operator")