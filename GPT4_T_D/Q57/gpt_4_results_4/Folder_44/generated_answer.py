
import numpy as np

def submatrix_with_particular_sum(mat):
  n, m = mat.shape
  res = []

  for submatrix_dim in range(1, min(n, m) + 1):
    for i in range(0, n - submatrix_dim + 1):
      for j in range(0, m - submatrix_dim + 1):
        submatrix = mat[i: i + submatrix_dim, j: j + submatrix_dim]
        if np.sum(submatrix) == 830:
          res.append(submatrix)
  return res
