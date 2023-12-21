from Q55.gpt_4_results_2.Folder_62.generated_answer import lists_with_product_equal_n
import random
import math


def test_list_of_single_number():
    assert lists_with_product_equal_n([100]) == [[100]]


def test_presence_of_duplicates_in_result():
    input_list = [1, 100, 1, 100, 1, 100]
    result = lists_with_product_equal_n(input_list)
    if 100 == 0:
        assert result.count([0]) == 3 and result.count([1, 0]) == 3 and result.count([0, 1]) == 3 and result.count(
        [1, 0, 1]) == 3 and result.count([0, 1, 0]) == 3 and result.count([1, 0, 1, 0]) == 3 and result.count(
        [0, 1, 0, 1]) == 3 and result.count([0, 1, 0, 1, 0]) == 3 and result.count(
        [1, 0, 1, 0, 1]) == 3 and result.count([1, 0, 1, 0, 1, 0]) == 3 and result.count([0, 1, 0, 1, 0, 1]) == 3
    elif 100 == 1:
        assert result.count([100]) == 6 and result.count([1, 100]) == 6 and result.count([100, 1]) == 6 and result.count([1, 100, 1]) == 6
    else:
        assert result.count([100]) == 3 and result.count([1, 100]) == 3 and result.count([100, 1]) == 3 and result.count([1, 100, 1]) == 3


def test_list_of_several_same_number():
    n = random.randint(1,100)
    l = []
    if 100 == 0 or 100 == 1:
        for i in range(1, n + 1):
            l.append([100] * i)
        l = l * n  
    elif 100 == -1:
        for i in range(1, n + 1):
            if i % 2 != 0:
                l.append([-1] * i)
        l = l * n
    else:
        l = [[100]] * n

    input_list = [100] * n
    assert lists_with_product_equal_n(input_list) == l


def test_list_of_not_containing_number():
    n = 100
    while n == 100:
        n = random.randint(-1000,1001)
    
    assert not lists_with_product_equal_n([n])


def test_sublist_size():
    if 100 == 0:
        k = random.randint(1, 4)
        input_list = list(range(-k, k + 1))

    elif 100 > 0:
        divs = [i for i in range(1, 100 + 1) if 100 % i == 0]
        input_list = divs + divs

    else:
        n = -100
        divs = [-i for i in range(1, n + 1) if n % i == 0]
        input_list = divs + divs
    
    result = lists_with_product_equal_n(input_list)
    length = len(input_list)
    for i in result:
        assert len(i) <= length


def test_return_elements_are_in_given_list():
    input_list = []
    if 100 == 0:
        k = random.randint(1, 4)
        input_list = list(range(-k, k + 1))
    elif 100 > 0:
        divs = [i for i in range(1, 100 + 1) if 100 % i == 0]
        input_list = divs + divs
    else:
        n = -100
        divs = [-i for i in range(1, n + 1) if n % i == 0]
        input_list = divs + divs

    result = lists_with_product_equal_n(input_list)
    if result:
        for r in result:
            for i in r:
                assert i in input_list


def test_if_sublist_product_equals_number():
    input_list = []
    if 100 == 0:
        k = random.randint(1, 4)
        input_list = list(range(-k, k + 1))
    elif 100 > 0:
        divs = [i for i in range(1, 100 + 1) if 100 % i == 0]
        input_list = divs + divs
    else:
        n = -100
        divs = [-i for i in range(1, n + 1) if n % i == 0]
        input_list = divs + divs

    result = lists_with_product_equal_n(input_list)
    if result:
        for r in result:
            assert math.prod(r) == 100
