def rotate(nums: list[int], k: int) -> None:
    l = len(nums)
    nums2 = nums.copy()

    for i in range(0, l):
        nums[(i + k) % l] = nums2[i]


nums = [1,2,3,4,5,6,7]
k = 3
print(f"nums: {nums}, k: {k}")
rotate(nums, k)
print(f"nums: {nums}")
print("")

nums = [-1,-100,3,99]
k = 2
print(f"nums: {nums}, k: {k}")
rotate(nums, k)
print(f"nums: {nums}")

