def characterReplacement(s: str, k: int) -> int:
    state = [0] * 26
    left = 0
    max_ = 0

    for right in range(len(s)):
        state[ord(s[right]) - 65] += 1

        while (right - left + 1) - max(state) > k:
          # repeatedly contract window until it is valid again
          # remove nums[start] from state in O(1) in time
          state[ord(s[left]) - 65] -= 1
          left += 1

        # INVARIANT: state of current window is valid here.
        max_ = max(max_, right - left + 1)

    return max_


s = "ABAB"
k = 2
print(characterReplacement(s, k))
s = "AABABBA"
k = 1
print(characterReplacement(s, k))