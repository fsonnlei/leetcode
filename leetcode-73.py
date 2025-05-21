def setZeroes0(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    firstRow = False
    firstCol = False

    for i in range(0, rows):
        for j in range(0, cols):
            if matrix[i][j] == 0:
                if i == 0:
                    firstRow = True
                if j == 0:
                    firstCol = True
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if firstRow:
        for j in range(0, cols):
            matrix[0][j] = 0

    if firstCol:
        for i in range(0, rows):
            matrix[i][0] = 0


def setZeroes1(matrix):
    rows = set()
    columns = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.add(i)
                columns.add(j)

    print(rows, columns)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in rows or j in columns:
                matrix[i][j] = 0



matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(matrix)
setZeroes1(matrix)
print(matrix)
print("")
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(matrix)
setZeroes1(matrix)
print(matrix)
