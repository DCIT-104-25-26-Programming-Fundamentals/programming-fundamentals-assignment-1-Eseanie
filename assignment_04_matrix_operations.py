
A = [[2,3,4], [4,5,7]]
B = [[1,4,6], [2,9,3]]
C = [[2,3,4],[4,5,7],[2,9,3]]



def transposeMatrix(mtx):
    rows = len(mtx)
    cols = len(mtx[0])

    result_total = []

    for col in range(cols):
        new_row = []
        for row in range(rows):
            new_row.append(mtx[row][col])
        result_total.append(new_row)

    print(result_total)


def add_matrices(A, B):
    rows  = len(A)
    cols = len(A[0])

    result_total = []

    for row in range(rows):
        new_row = []
        for col in range(cols):
            new_row.append(A[row][col] + B[row][col])
        result_total.append(new_row)

    print(result_total)


def multiply_matrices(A, B):
    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

    if colsA != rowsB:
        print("cannot multiply because it's not the same.")
        return None

    result_total = []

    for i in range(rowsA):
        new_row = []

        for j in range(colsB):
            total = 0
            for k in range(colsA):
                total += A[i][k] * B[k][j]
            new_row.append(total)
        result_total.append(new_row)
    print(result_total)


print("Print Part A")
transposeMatrix(A)

print("print part B")
add_matrices(A, B)

print("print part C")
multiply_matrices(A, C)