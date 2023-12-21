
def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix[0])):
            curr_sum = 0
            for k in range(i, j):
                for l in range(k, len(matrix[0])):
                    curr_sum += matrix[k][l]
                    if curr_sum == 78:
                        result.append((i, j))
    return result
