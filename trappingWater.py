def trappingWater(height: list[int]):
    l_wall = r_wall = 0
    n = len(height)
    max_left = [0] * n
    max_right = [0] * n
    j = n - 1

    for i in range(n):
        max_left[i] = l_wall
        max_right[j] = r_wall
        l_wall = max(l_wall, height[i])
        r_wall = max(r_wall, height[j])
        j = j - 1

    summ = 0
    for i in range(n):
        pot = min(max_left[i], max_right[i])
        if pot > height[i]:
            summ += pot - height[i]

    return summ

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trappingWater(height))