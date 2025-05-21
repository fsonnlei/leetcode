def generateMatrix(n: int) -> list[list[int]]:
    matrix = [[0] * n for _ in range(n)]

    print(f"generate matrix with {n} rows and {n} columns")

    top, bottom = 0, n - 1
    left, right = 0, n - 1

    my_n = 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            matrix[top][i] = my_n
            my_n += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = my_n
            my_n += 1
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = my_n
                my_n += 1
            bottom -= 1

        if left <= right:
            # Traverse from Bottom to Top
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = my_n
                my_n += 1
            left += 1

    print(matrix)
    print("")

n = 3
generateMatrix(n)

n = 1
generateMatrix(n)