
def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    
    for i in range(rows-180+1):
        for j in range(cols-180+1):
            if all([all([180 in row[j:j+180] for row in matrix[i:i+180]])]):
                count += 1
    
    return count
