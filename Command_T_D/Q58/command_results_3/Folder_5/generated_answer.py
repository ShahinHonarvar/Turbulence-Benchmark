import numpy as np
def submatrix_with_n_numbers(nums):
    return sum(np.vectorize(lambda x: len(x) == 63)(x) for x in np.nditer(nums))
