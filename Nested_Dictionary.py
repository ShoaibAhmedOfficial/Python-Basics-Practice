course={
    'php':{'duration':'2Months','fee':2000},
    'java':{'duration':'2 Months', 'fee':3000},
    'python':{'duration':'2Months', 'fee':4000}
}
print(course['php']['fee'])
course['java']['fee']= 30000
for k,c in course.items():
    print(k,c['duration'],c['fee'])