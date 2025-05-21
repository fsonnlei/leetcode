def canJump(nums: list[int]) -> bool:
    max_reach = 0

    for i in range(len(nums)):
        if i > max_reach:
            return False

        max_reach = max(max_reach, i + nums[i])

        if max_reach >= len(nums) - 1:
            return True

    return True


nums = [2,3,1,1,4]
print(f"{canJump(nums)}")
nums = [3,2,1,0,4]
print(f"{canJump(nums)}")
nums = [1]
print(f"{canJump(nums)}")
nums = [1,2]
print(f"{canJump(nums)}")
nums = [0]
print(f"{canJump(nums)}")
nums = [0,1]
print(f"{canJump(nums)}")
