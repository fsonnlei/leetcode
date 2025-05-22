def checkPowersOfThree(n: int) -> bool:
    while (n):
        if n % 3 == 2: # 2 < 3
            return False
        n //= 3
    return True

n = 12
print(checkPowersOfThree(n))

n = 16
print(checkPowersOfThree(n))

n = 21
print(checkPowersOfThree(n))
