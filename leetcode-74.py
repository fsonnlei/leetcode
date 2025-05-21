def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])
    t = rows * cols
    left = 0
    right = t - 1

    while left <= right:
        mid = (left + right) // 2
        mid_i = mid // cols
        mid_j = mid % cols
        number = matrix[mid_i][mid_j]
        print(f"matrix[{mid_i},{mid_j}] = {number}, middle = {mid}, total = {t}")

        if number == target:
            return True
        elif number < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix, target))
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(searchMatrix(matrix, target))

