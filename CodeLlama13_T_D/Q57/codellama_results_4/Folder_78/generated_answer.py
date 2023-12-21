
def submatrix_with_particular_sum(matrix):
    submatrices = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            current_submatrix = [[matrix[i][j] for j in range(col, len(matrix[row]))] for i in range(row, len(matrix))]
            if sum(map(sum, current_submatrix)) == 17:
                submatrices.append(current_submatrix)
    return submatrices
