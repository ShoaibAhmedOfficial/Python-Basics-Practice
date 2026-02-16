import random
a=random.randint(2,5)
print(a)
a=random.randrange(2,3)
print(a)
l=[1,2,3,4,5,6,7,7]
# n=random.choice(l)
print(random.choice(l))
print(random.random())
l=[1,2,3,45]
random.shuffle(l)
print(l)
u=random.uniform(2,4)
print(u)