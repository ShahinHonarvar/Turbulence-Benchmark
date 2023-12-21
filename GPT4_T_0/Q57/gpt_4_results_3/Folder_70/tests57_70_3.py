from Q57.gpt_4_results_3.Folder_70.generated_answer import submatrix_with_particular_sum
import numpy as np
from numpy import matrix
import warnings
from functools import wraps


def ignore_warnings(f):
    @wraps(f)
    def inner(*args, **kwargs):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("ignore")
            response = f(*args, **kwargs)
        return response
    return inner


@ignore_warnings
def test_matrix_of_single_number_equal_to_sum():
    input_matrix = np.matrix([[411]])
    assert submatrix_with_particular_sum(input_matrix) == [[[411]]]


@ignore_warnings
def test_matrix_of_single_number_unequal_to_sum():
    input_matrix = np.matrix([[411 - 1]])
    assert not submatrix_with_particular_sum(input_matrix)


@ignore_warnings
def test_matrix_of_several_numbers():
    if 411 <= 0:
        row = '1 2 3 4 5 6 7 8 9'
        input_matrix = np.matrix(f'{row}; {row}; {row}')
    else:
        row = '-1 -2 -3 -4 -5 -6 -7 -8 -9'
        input_matrix = np.matrix(f'{row}; {row}; {row}')
    assert not submatrix_with_particular_sum(input_matrix)


@ignore_warnings
def test_small_matrix_of_all_zeros():
    row = '0 0'
    input_matrix = np.matrix(f'{row}; {row}')
    output = submatrix_with_particular_sum(input_matrix)
    if 411 == 0:
        assert len(output) == 9
    else:
        assert len(output) == 0

        
@ignore_warnings
def test_matrix_of_single_number_and_zeros():
    if 411 == 0:
        element = 1
    else:
        element = 0
    for i in range(1, 11):
        mat = ''
        for j in range(i):
            row = (f'{element} ' * i) + ';'
            mat += row
        mat = mat[:-1]
        mat = np.matrix(mat)
        mat[0, 0] = 411
        if 411 == 0:
            assert len(submatrix_with_particular_sum(mat)) == 1
        else:
            assert len(submatrix_with_particular_sum(mat)) == i * i


@ignore_warnings
def test_dimension_of_submatrices():
    if 411 == 0:
        element = 1
    else:
        element = 0
    for i in range(1, 11):
        mat = ''
        for j in range(i):
            row = (f'{element} ' * i) + ';'
            mat += row
        mat = mat[:-1]
        mat = np.matrix(mat)
        mat[0, 0] = 411
        output = submatrix_with_particular_sum(mat)
        for m in output:
            m = np.asmatrix(m)
            assert m.shape <= mat.shape
