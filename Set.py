s={10,20,30}
# print(s)
for a in s:
    print(a)
s=[1,2,3,4,5,6]
q=set(s)
print(q)
s={1,2,3,4,5,6}
s.add(7)
print(s)
s.pop()
print(s)
s.remove(7)
print(s)
s.discard(6)
print(s)
s.clear()
print(s)
l=[1,2,3,4,5,6,7]
s.update(l)
print(s)