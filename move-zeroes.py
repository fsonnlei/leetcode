def moveZeroes(nums: list[int]):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j = j + 1
            print(nums)
    return nums




nums = [2,0,4,0,9]
print(nums)
print(moveZeroes(nums))
# Output: [2,4,9,0,0]

nums = [0,0,1]
print(nums)
print(moveZeroes(nums))
