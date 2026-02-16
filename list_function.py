# del
# pop()
# remove()
# clear()

s=[1,2,3,4,5]
del s[1]
print(s)

s=[2,4,5,6,7,7,8]
s.pop(4)
print(s.pop(4))
print(s)

s=[2,34,45,23,234,34,34,34343]
s.remove(45)
# print(s.remove(45))
print(s)

s.clear()
print(s)

a=[10,20,30,40,50]
a[3]=44
print(a)
a.insert(0,0)
print(a)
a.append(60)
print(a)
n=[70]
a.extend(n)
print(a)

l=[1,2,3,4,5,6,7,1,1]
a=l.count(1)
print(a)

m=max(l)
print(m)

a=min(l)
print(a)

l.sort()
print(l)

l.reverse()
print(l)

a=l.index(7)
print(a)
