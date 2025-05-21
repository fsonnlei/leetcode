def jump(nums: list[int]) -> int:
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest

    return jumps




nums = [2,3,1,1,4]
print(jump(nums))
nums = [2,3,0,1,4]
print(jump(nums))
nums = [1,2,1,1,1]
print(jump(nums))
nums = [0]
print(jump(nums))
nums = [1]
print(jump(nums))
nums = [1,2]
print(jump(nums))
nums = [3,2,1]
print(jump(nums))



