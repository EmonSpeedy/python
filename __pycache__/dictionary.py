
person = {'Name' : 'Emon', 'Address' : 'New Jersy', 'Age' : 21, 'Job' : 'Soft Engr'}
print(person)

print(person['Job'])
print(person.keys())
print(person.values())
person['Sex'] = 'Male'
print(person)

del person['Age']
print(person)

for key, value in person.items():
    print(key," : ", value)

