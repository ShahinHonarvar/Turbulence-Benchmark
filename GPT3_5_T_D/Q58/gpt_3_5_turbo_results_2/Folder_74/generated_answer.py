
def submatrix_with_n_numbers(matrix):
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    if (k-i+1) * (l-j+1) == 48:
                        count += 1
                        
    return count
