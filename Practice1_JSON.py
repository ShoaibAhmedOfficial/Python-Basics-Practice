import json

d = '{"name": "Python", "fee": 12000, "Duration": "2 Months"}'

x=json.loads(d)
print(type(x))
print(x)

for a in x:
    print(a, x[a])