
def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 192):
        for j in range(cols - 192):
            submatrix = matrix[i:i + 193, j:j + 193]
            if np.all(submatrix == 193):
                count += 1
    return count
