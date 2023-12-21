from Q55.codellama_results_2.Folder_91.generated_answer import lists_with_product_equal_n
import random
import math


def test_list_of_single_number():
    assert lists_with_product_equal_n([2]) == [[2]]


def test_presence_of_duplicates_in_result():
    input_list = [1, 2, 1, 2, 1, 2]
    result = lists_with_product_equal_n(input_list)
    if 2 == 0:
        assert result.count([0]) == 3 and result.count([1, 0]) == 3 and result.count([0, 1]) == 3 and result.count(
        [1, 0, 1]) == 3 and result.count([0, 1, 0]) == 3 and result.count([1, 0, 1, 0]) == 3 and result.count(
        [0, 1, 0, 1]) == 3 and result.count([0, 1, 0, 1, 0]) == 3 and result.count(
        [1, 0, 1, 0, 1]) == 3 and result.count([1, 0, 1, 0, 1, 0]) == 3 and result.count([0, 1, 0, 1, 0, 1]) == 3
    elif 2 == 1:
        assert result.count([2]) == 6 and result.count([1, 2]) == 6 and result.count([2, 1]) == 6 and result.count([1, 2, 1]) == 6
    else:
        assert result.count([2]) == 3 and result.count([1, 2]) == 3 and result.count([2, 1]) == 3 and result.count([1, 2, 1]) == 3


def test_list_of_several_same_number():
    n = random.randint(1,100)
    l = []
    if 2 == 0 or 2 == 1:
        for i in range(1, n + 1):
            l.append([2] * i)
        l = l * n  
    elif 2 == -1:
        for i in range(1, n + 1):
            if i % 2 != 0:
                l.append([-1] * i)
        l = l * n
    else:
        l = [[2]] * n

    input_list = [2] * n
    assert lists_with_product_equal_n(input_list) == l


def test_list_of_not_containing_number():
    n = 2
    while n == 2:
        n = random.randint(-1000,1001)
    
    assert not lists_with_product_equal_n([n])


def test_sublist_size():
    if 2 == 0:
        k = random.randint(1, 4)
        input_list = list(range(-k, k + 1))

    elif 2 > 0:
        divs = [i for i in range(1, 2 + 1) if 2 % i == 0]
        input_list = divs + divs

    else:
        n = -2
        divs = [-i for i in range(1, n + 1) if n % i == 0]
        input_list = divs + divs
    
    result = lists_with_product_equal_n(input_list)
    length = len(input_list)
    for i in result:
        assert len(i) <= length


def test_return_elements_are_in_given_list():
    input_list = []
    if 2 == 0:
        k = random.randint(1, 4)
        input_list = list(range(-k, k + 1))
    elif 2 > 0:
        divs = [i for i in range(1, 2 + 1) if 2 % i == 0]
        input_list = divs + divs
    else:
        n = -2
        divs = [-i for i in range(1, n + 1) if n % i == 0]
        input_list = divs + divs

    result = lists_with_product_equal_n(input_list)
    if result:
        for r in result:
            for i in r:
                assert i in input_list


def test_if_sublist_product_equals_number():
    input_list = []
    if 2 == 0:
        k = random.randint(1, 4)
        input_list = list(range(-k, k + 1))
    elif 2 > 0:
        divs = [i for i in range(1, 2 + 1) if 2 % i == 0]
        input_list = divs + divs
    else:
        n = -2
        divs = [-i for i in range(1, n + 1) if n % i == 0]
        input_list = divs + divs

    result = lists_with_product_equal_n(input_list)
    if result:
        for r in result:
            assert math.prod(r) == 2
