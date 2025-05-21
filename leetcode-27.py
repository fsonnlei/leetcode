def removeElement(self, nums: list[int], val: int) -> int:
    j = 0

    for i in range(len(nums)):
        if (nums[i] != val):
                nums[j] = nums[i]
                j += 1
    return j

nums = [3,2,2,3]
val = 3
print(f"Counter: {removeElement(nums, nums, val)}")
print(f"nums: {nums}")
print("")

nums = [0,1,2,2,3,0,4,2]
val = 2
print(f"Counter: {removeElement(nums, nums, val)}")
print(f"nums: {nums}")

print("Done!")