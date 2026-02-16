a=[]
for l in range(1,101):
    a.append(l)

print(a)
print('1 to 100')
print("")
a=[n for n in range(1,101) if n%2==0 ]
print(a)
print('This is even number')
print("")
a=[n for n in range(1,101) if n%2==1 ]
print(a)
print('This is odd number')
print("")

s='hello'
d=[g for g in s]
print(d)
