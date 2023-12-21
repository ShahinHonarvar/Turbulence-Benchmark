def submatrix_with_particular_sum(matrix):
    return [x for x in [[y[i:j] for i in range(len(y)))] for y in zip(*matrix) if len(y) > 1 and sum(y) == -59]
