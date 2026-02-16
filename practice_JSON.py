import json

d = {
    'course_name': 'Python',
    'fee':1500
}

f=json.dumps(d)
print(f)