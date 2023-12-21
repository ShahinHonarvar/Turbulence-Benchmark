
def submatrix_with_n_numbers(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    
    count = 0
    
    for i in range(rows - 3):
        for j in range(cols - 3):
            submatrix = matrix[i:i+4, j:j+4]
            
            if np.sum(submatrix) == 49:
                count += 1
                
    return count
