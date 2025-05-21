def maxSum(nums: list[int], k: int):
    state =  0
    left = 0
    max_ = 0

    for right in range(len(nums)):
        # extend window
        # add nums[end] to state in O(1) in time
        state += nums[right]
        if right - left + 1 == k:
            # INVARIANT: size of the window is k here.
            max_ = max(max_, state)

            # contract window
            # remove nums[start] from state in O(1) in time
            state -= nums[left]
            left += 1

    return max_


nums = [2, 1, 5, 1, 3, 2]
k = 3
print(maxSum(nums, k))