
import numpy as np

def submatrix_with_particular_sum(mtrx):
    output = []
    rows, cols = mtrx.shape
    for x in range(rows):
        for y in range(cols):
            for width in range(0, cols - y + 1):
                for height in range(0, rows - x + 1):
                    submatrix = mtrx[x:x + height, y:y + width]
                    if np.sum(submatrix) == -863:
                        output.append(submatrix.tolist())
    return output
