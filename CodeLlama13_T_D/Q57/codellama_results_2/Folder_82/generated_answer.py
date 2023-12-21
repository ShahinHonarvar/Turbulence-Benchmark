
def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            current_row = matrix[i, :]
            current_col = matrix[:, j]
            current_submatrix = matrix[i:i+2, j:j+2]
            if (current_row.sum() + current_col.sum() - 2*current_submatrix.sum()) == -27:
                return current_submatrix
    return []
