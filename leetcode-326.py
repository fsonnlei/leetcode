def isPowerOfThree(n: int) -> bool:
    if n < 1:
        return False
    while n % 3 == 0:
        n = n // 3
    return n == 1

n = 243
print(isPowerOfThree(n))

n = 1
print(isPowerOfThree(n))

n = 2
print(isPowerOfThree(n))

n = -1
print(isPowerOfThree(n))
