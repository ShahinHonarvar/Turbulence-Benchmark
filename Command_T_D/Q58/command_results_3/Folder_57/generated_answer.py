import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(
        np.sum(
            np.sum(
                np.sum(
                    np.all(
                        np.all(
                            np.all(
                                np.count_nonzero(
                                    matrix
                                )
                            )
                        )
                    )
                )
            )
        )
    )
