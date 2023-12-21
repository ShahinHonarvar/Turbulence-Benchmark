
def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    
    for i in range(rows-99+1):
        for j in range(cols-99+1):
            submatrix = matrix[i:i+99,j:j+99]
            if np.all(submatrix == 99):
                count += 1
                
    return count
