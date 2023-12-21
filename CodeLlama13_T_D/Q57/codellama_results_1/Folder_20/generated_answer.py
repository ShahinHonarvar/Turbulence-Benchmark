
def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            current_row, current_col = i, j
            while current_row < rows and current_col < cols:
                submatrix = matrix[current_row:i+1, current_col:j+1]
                if submatrix.sum() == -57:
                    return list(submatrix)
                current_row += 1
                current_col += 1
    return []
