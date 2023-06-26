
nums = [12, 23, 12, 54, 67, 23, 17, 12]
# print(len(nums))

Set = set(nums)
print(Set)

Set.add(644)
print(Set)
Set.remove(17)
print(Set)

for n in Set:
    print(n)

if 6449 in Set:
    print("Exists")
else:
    print("Not Exists")

A = {1,2,3}
B = {1,2,3,4,5,6}

print(A & B)
print(A | B)

