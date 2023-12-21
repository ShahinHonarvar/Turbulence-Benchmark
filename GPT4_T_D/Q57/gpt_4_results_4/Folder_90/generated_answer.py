
import numpy as np

def submatrix_with_particular_sum(mat):
    result = []
    numRows,numCols = mat.shape
    for startRow in range(numRows):
        for startCol in range(numCols):
            for endRow in range(startRow,numRows):
                for endCol in range(startCol,numCols):
                    submatrix = mat[startRow:endRow+1,startCol:endCol+1]
                    if np.sum(submatrix) == -452:
                        result.append(submatrix.tolist())
    return result
