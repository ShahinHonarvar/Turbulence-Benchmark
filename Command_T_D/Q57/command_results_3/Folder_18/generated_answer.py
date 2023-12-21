def submatrix_with_particular_sum(matrix):
    rows = [r for r in range(matrix.shape[0])]
    columns = [c for c in range(matrix.shape[1])]
    return [matrix[r][:c] + matrix[r][c + 1 :] + matrix[:r][c] + matrix[r + 1 :][c] for r in rows for c in columns if matrix[r][c] == 616]
