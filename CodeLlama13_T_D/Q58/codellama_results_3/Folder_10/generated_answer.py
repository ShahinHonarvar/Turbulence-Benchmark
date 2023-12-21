
def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows-4):
        for j in range(cols-4):
            if all([sum(row[j:j+5]) == 56 for row in matrix[i:i+5]]):
                count += 1
    return count
