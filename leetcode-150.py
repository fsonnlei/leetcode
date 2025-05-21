def mymerge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1[m:m+n] = nums2
    nums1.sort()
    return None

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

mymerge(nums1, nums1, m, nums2, n)
print(nums1)

nums1 = [1]
m = 1
nums2 = []
n = 0
mymerge(nums1, nums1, m, nums2, n)
print(nums1)

nums1 = [0]
m = 0
nums2 = [1]
n = 1
mymerge(nums1, nums1, m, nums2, n)
print(nums1)

print("Done!")