def removeDuplicates(nums: list[int]) -> int:
    i = 1
    j = 0

    while i < len(nums):
        if nums[j] != nums[i]:
            j += 1
            nums[j] = nums[i]
        i +=1

    return j+1


nums = [1,1,2]
print(f"nums: {nums}")
print(f"removeDuplicates: {removeDuplicates(nums)}")
print(f"nums: {nums}")
print("")

nums = [0,0,1,1,1,2,2,3,3,4]
print(f"nums: {nums}")
print(f"removeDuplicates: {removeDuplicates(nums)}")
print(f"nums: {nums}")
print("")

