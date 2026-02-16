p={
    'name':'python',
    'fee': '600',
    'Duration': '2months'
}
n=p.get('name')
a=p.get('fee')
print(n,a)
print()
for q in p.keys():
    print(q)
print()
for w in p.values():
    print(w)
print()
for e in p.items():
    print(e)
print()
del p['fee']
print(p)
r=p.pop('Duration')
print(r)

d=dict(name='python',fees='800')
print(d)

z={
    'hb':'duration',
    'fee': 9000,
}
z.update({'fee':43434343})
print(z)
z['duration']="2months"
print(z )

