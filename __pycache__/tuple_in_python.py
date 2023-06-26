
def multi():
    return 1, 2
# print(multi())

things = 'egg', 'sugar', 'rice', 'chicken', 'milk', 'tomato'

for item in things:
    print(item)

if 'rice' in things:
    print("Exists")
else:
    print("Not Exists")

print(things[3])
print(things[-2])

print(things[1:4])
print(len(things))

mega = ([1,2,3], [4,5,6])
# print(type(mega))
print(mega[1])
mega[1][0] = 144
print(mega[1])
