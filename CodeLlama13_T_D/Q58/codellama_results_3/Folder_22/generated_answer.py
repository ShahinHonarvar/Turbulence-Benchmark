
def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 20 + 1):
        for j in range(cols - 20 + 1):
            submatrix = matrix[i:i+20,j:j+20]
            if (submatrix == 21).all():
                count += 1
    return count
