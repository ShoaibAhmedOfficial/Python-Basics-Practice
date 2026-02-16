# Range(5)
# #Start=0
# #condition<5
# #increment 1
# Value: 0 1 2 3 4
#
# Range (1,6)
# Start=1
# Condition<6
# Increment 1
# Value: 1,2,3,4,5
#
# Range (1,6,2)
# Start=1
# Condition<6
# Increment 2
# Value: 1 3 5

#
# a=int(input("Enter the number between 1 to 10: "))
# # b=int(input("Enter the value for loop start between 1 to 10: "))
# # c=int(input("Increment value in for loop range: "))
# if a>12:
#     for n in range(a):
#         print(n)
# # elif b>0<10:
# #         print("Enter the value between 1 to 10")
# else:
#     print("enter the number between 1 to 10")

a=int(input("Input the number: "))
for n in range(1,11,1):
    print(a ," * ", n, " = ", a*n)
print()
for n in range(12,1,-2):
    print(n)
