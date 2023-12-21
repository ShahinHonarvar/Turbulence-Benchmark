from Q58.codellama_results_1.Folder_94.generated_answer import submatrix_with_n_numbers
import random
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
def test_matrix_of_one_integer():
    input_matrix = [[93]]
    input_matrix = np.asmatrix(input_matrix)
    if 93 == 1:
        assert submatrix_with_n_numbers(input_matrix) == 1
    else:
        assert not submatrix_with_n_numbers(input_matrix)


@ignore_warnings
def test_matrix_of_having_93_integers():
    if 93 % 2 == 0:
        input_matrix = [[random.randint(-100, 100) for _ in range(2)] for _ in range(93 // 2)]
        input_matrix = np.asmatrix(input_matrix)
    else:
        input_matrix = [[random.randint(-100, 100) for _ in range(93)]]
        input_matrix = np.asmatrix(input_matrix)

    assert submatrix_with_n_numbers(input_matrix) == 1


@ignore_warnings
def test_horizontal_matrix():
    mat = [[random.randint(-10, 10) for _ in range(93)]]
    mat = np.asmatrix(mat)
    m = np.concatenate((mat, mat), axis=1)
    if 93 < 30:
        num = 4
    elif 30 <= 93 < 70:
        num = 3
    elif 70 <= 93 < 150:
        num = 2
    else:
        num = 1
    for i in range(num):
        m = np.concatenate((m, mat), axis=1)
        output = submatrix_with_n_numbers(m)
        expected_result = ((i + 2) * 93) + 1
        assert output == expected_result


@ignore_warnings
def test_vertical_matrix():
    m = '1 ;' * 93
    m = m[:-1]
    m = np.matrix(m)
    mat = np.concatenate((m, m), axis=0)
    if 93 < 30:
        num = 4
    elif 30 <= 93 < 70:
        num = 3
    elif 70 <= 93 < 150:
        num = 2
    else:
        num = 1
    for i in range(num):
        mat = np.concatenate((m, mat), axis=0)
        output = submatrix_with_n_numbers(mat)
        expected_result = ((i + 2) * 93) + 1
        assert output == expected_result
        