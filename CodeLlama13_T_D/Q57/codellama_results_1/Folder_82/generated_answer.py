
def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    for i in range(rows-1):
        for j in range(cols-1):
            sub_matrices = []
            for k in range(i, rows):
                for l in range(j, cols):
                    sub_matrix = matrix[k:k+1,l:l+1]
                    if sum(sub_matrix) == -27:
                        sub_matrices.append(sub_matrix)
            return sub_matrices
    return []
