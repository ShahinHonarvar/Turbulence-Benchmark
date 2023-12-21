
def submatrix_with_particular_sum(matrix):
    sum_of_integers = 0
    for row in matrix:
        for element in row:
            sum_of_integers += int(element)
    if sum_of_integers == 93:
        return [matrix]
    else:
        return []
