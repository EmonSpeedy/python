
nums = [11, 34, 22, 45, 20]

nums.append(25)
print(nums)

nums.insert(1, 40)
print(nums)

if 23 in nums:
    nums.remove(23)
    print(nums)

last = nums.pop()
print(last, nums)

idx = nums.index(45)
print(idx)

nums.sort()
print(nums)
nums.reverse()
print(nums)
