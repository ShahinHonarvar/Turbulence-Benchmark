def submatrix_with_particular_sum(arr):
    return [[row[i] for i in range(len(row)) if sum(row) == 997] for row in zip(*arr)]
