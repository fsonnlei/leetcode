from collections import defaultdict


def totalFruit(fruits: list[int]) -> int:
    max_length = 0

    for i in range(len(fruits)):
        state = defaultdict(int)
        for j in range(i, len(fruits)):
            state[fruits[j]] += 1
            print(state)
            if len(state) <= 2: # 2 baskets!!!!!
                max_length = max(max_length, j - i + 1) # j - i +1 = length of the window
            else:
                break

    return max_length


fruits = [1,2,1]
print(fruits)
print(totalFruit(fruits))
fruits = [3, 3, 2, 1, 2, 1, 0]
print(fruits)
print(totalFruit(fruits))

""" template """
# Here's a template you can use as a starting point for solving problems with a variable-length sliding window.
"""
def variable_length_sliding_window(nums):
  state = # choose appropriate data structure
  start = 0
  max_ = 0

  for end in range(len(nums)):
    # extend window
    # add nums[end] to state in O(1) in time

    while state is not valid:
      # repeatedly contract window until it is valid again
      # remove nums[start] from state in O(1) in time
      start += 1

    # INVARIANT: state of current window is valid here.
    max_ = max(max_, end - start + 1)

  return max_
"""