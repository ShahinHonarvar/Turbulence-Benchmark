
def submatrix_with_n_numbers(matrix):
    n = 24
    count = 0
    for i in range(len(matrix) - n + 1):
        for j in range(len(matrix[i]) - n + 1):
            if all([sum(row[j:j+n]) == n*24 for row in matrix[i:i+n]]):
                count += 1
    return count
