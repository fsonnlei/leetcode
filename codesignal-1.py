def new_array(a: list[int]) -> list[int]:

    n = len(a)
    result = [0] * n

    for i in range(n):
        if i-1 >= 0:
            result[i]+=a[i-1]

        result[i]+=a[i]

        if i+1 < n:
            result[i]+=a[i+1]

    return result

a = [4,0,1,-2,3]
b = new_array(a)
print(a)
print(b)