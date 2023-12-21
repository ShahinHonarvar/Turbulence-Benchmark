def submatrix_with_particular_sum(matrix):
    return [[y[x:x + 8] for x in range(len(y) - 7)] for y in matrix]
