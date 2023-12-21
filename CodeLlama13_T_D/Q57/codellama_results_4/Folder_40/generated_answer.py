
def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == -10:
                submatrices.append([matrix[i][j]])
    return submatrices
