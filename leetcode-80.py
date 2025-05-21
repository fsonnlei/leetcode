def removeDuplicates(nums: list[int]) -> int:
    i = 2  # Start from index 2 since the first two can always stay
    for j in range(2, len(nums)):
        if nums[j] != nums[i - 2]:
            nums[i] = nums[j]
            i += 1
    return i

nums = [1,1,1,2,2,3]
print(f"nums: {nums}")
k = removeDuplicates(nums)
for i in range(k, len(nums)):
    nums.pop(i-1)
print(f"removeDuplicates: {k}")
print(f"nums: {nums}")
print("")

nums = [0,0,1,1,1,1,2,3,3]
print(f"nums: {nums}")
k = removeDuplicates(nums)
for i in range(k, len(nums)):
    nums.pop(i-1)
print(f"removeDuplicates: {k}")
print(f"nums: {nums}")
print("")
