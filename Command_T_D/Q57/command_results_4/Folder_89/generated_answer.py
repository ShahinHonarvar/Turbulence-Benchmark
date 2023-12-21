def submatrix_with_particular_sum(matrix):
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    submatrices = []
    for row in range(rows):
        for column in range(columns):
            row_matrix = matrix[row][:column] + matrix[row][column+1:]
            row_matrix += matrix[:row][:column] + matrix[:row][column+1:]
            row_matrix += matrix[rows-1][:column] + matrix[rows-1][column+1:]
            if len(row_matrix) == 80:
                submatrices.append(row_matrix)
    return submatrices
