from itertools import count
from operator import index

q=(2,3,4,5)
l = len (q)
for a in range(l):
    print(q[a])
for w in q:
    print(w)
# min()
# max()
# count()
# index()
# sum()
p=(3,4,5,6,7,8,8)
z=min(p)
print(z)
x=max(p)
print(x)
c = p.count(8)
print(c)
v=p.index(8)
print(v)
b=sum(p)
print(b)
