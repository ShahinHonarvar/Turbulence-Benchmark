
def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sum_of_elements = 0
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    sum_of_elements += matrix[k][l]
                if sum_of_elements == 997:
                    result.append((i, j, k, l))
            sum_of_elements = 0
    return result
