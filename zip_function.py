l=[1,2,3,4,5,6,7,8,9]
l1=[10,20,30,40,50,60,70,80,90]

t=len(l)

for a,b in zip(l,l1):
    print(a,b)
print()
for h in range (t):
    print(l[h],l1[h])