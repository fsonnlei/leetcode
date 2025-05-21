def longestSubstringWithoutRepeat(s: str):
    state = set()
    left = 0
    max_ = 0

    for right in range(len(s)):
        while s[right] in state:
          # repeatedly contract window until it is valid again
          # remove nums[start] from state in O(1) in time
          state.remove(s[left])
          left += 1

        # INVARIANT: state of current window is valid here.
        max_ = max(max_, right - left + 1)
        state.add(s[right])

    return max_

s = "eghghhgg"
print(longestSubstringWithoutRepeat(s))
s = "abcabcbb"
print(longestSubstringWithoutRepeat(s))
s = "bbbbb"
print(longestSubstringWithoutRepeat(s))
s = "pwwkew"
print(longestSubstringWithoutRepeat(s))