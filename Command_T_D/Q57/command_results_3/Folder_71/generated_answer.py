def submatrix_with_particular_sum(matrix):
    return [submatrix for submatrix in [[row[i:j + 1] for i in range(len(row))] for row in matrix] if sum(submatrix) == 69]
