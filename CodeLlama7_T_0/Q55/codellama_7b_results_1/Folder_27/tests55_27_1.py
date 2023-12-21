from Q55.codellama_7b_results_1.Folder_27.generated_answer import lists_with_product_equal_n
import random
import math


def test_list_of_single_number():
    assert lists_with_product_equal_n([-82]) == [[-82]]


def test_presence_of_duplicates_in_result():
    input_list = [1, -82, 1, -82, 1, -82]
    result = lists_with_product_equal_n(input_list)
    if -82 == 0:
        assert result.count([0]) == 3 and result.count([1, 0]) == 3 and result.count([0, 1]) == 3 and result.count(
        [1, 0, 1]) == 3 and result.count([0, 1, 0]) == 3 and result.count([1, 0, 1, 0]) == 3 and result.count(
        [0, 1, 0, 1]) == 3 and result.count([0, 1, 0, 1, 0]) == 3 and result.count(
        [1, 0, 1, 0, 1]) == 3 and result.count([1, 0, 1, 0, 1, 0]) == 3 and result.count([0, 1, 0, 1, 0, 1]) == 3
    elif -82 == 1:
        assert result.count([-82]) == 6 and result.count([1, -82]) == 6 and result.count([-82, 1]) == 6 and result.count([1, -82, 1]) == 6
    else:
        assert result.count([-82]) == 3 and result.count([1, -82]) == 3 and result.count([-82, 1]) == 3 and result.count([1, -82, 1]) == 3


def test_list_of_several_same_number():
    n = random.randint(1,100)
    l = []
    if -82 == 0 or -82 == 1:
        for i in range(1, n + 1):
            l.append([-82] * i)
        l = l * n  
    elif -82 == -1:
        for i in range(1, n + 1):
            if i % 2 != 0:
                l.append([-1] * i)
        l = l * n
    else:
        l = [[-82]] * n

    input_list = [-82] * n
    assert lists_with_product_equal_n(input_list) == l


def test_list_of_not_containing_number():
    n = -82
    while n == -82:
        n = random.randint(-1000,1001)
    
    assert not lists_with_product_equal_n([n])


def test_sublist_size():
    if -82 == 0:
        k = random.randint(1, 4)
        input_list = list(range(-k, k + 1))

    elif -82 > 0:
        divs = [i for i in range(1, -82 + 1) if -82 % i == 0]
        input_list = divs + divs

    else:
        n = --82
        divs = [-i for i in range(1, n + 1) if n % i == 0]
        input_list = divs + divs
    
    result = lists_with_product_equal_n(input_list)
    length = len(input_list)
    for i in result:
        assert len(i) <= length


def test_return_elements_are_in_given_list():
    input_list = []
    if -82 == 0:
        k = random.randint(1, 4)
        input_list = list(range(-k, k + 1))
    elif -82 > 0:
        divs = [i for i in range(1, -82 + 1) if -82 % i == 0]
        input_list = divs + divs
    else:
        n = --82
        divs = [-i for i in range(1, n + 1) if n % i == 0]
        input_list = divs + divs

    result = lists_with_product_equal_n(input_list)
    if result:
        for r in result:
            for i in r:
                assert i in input_list


def test_if_sublist_product_equals_number():
    input_list = []
    if -82 == 0:
        k = random.randint(1, 4)
        input_list = list(range(-k, k + 1))
    elif -82 > 0:
        divs = [i for i in range(1, -82 + 1) if -82 % i == 0]
        input_list = divs + divs
    else:
        n = --82
        divs = [-i for i in range(1, n + 1) if n % i == 0]
        input_list = divs + divs

    result = lists_with_product_equal_n(input_list)
    if result:
        for r in result:
            assert math.prod(r) == -82
