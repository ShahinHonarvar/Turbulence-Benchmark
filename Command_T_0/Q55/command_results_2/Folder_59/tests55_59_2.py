from Q55.command_results_2.Folder_59.generated_answer import lists_with_product_equal_n
import random
import math


def test_list_of_single_number():
    assert lists_with_product_equal_n([-3]) == [[-3]]


def test_presence_of_duplicates_in_result():
    input_list = [1, -3, 1, -3, 1, -3]
    result = lists_with_product_equal_n(input_list)
    if -3 == 0:
        assert result.count([0]) == 3 and result.count([1, 0]) == 3 and result.count([0, 1]) == 3 and result.count(
        [1, 0, 1]) == 3 and result.count([0, 1, 0]) == 3 and result.count([1, 0, 1, 0]) == 3 and result.count(
        [0, 1, 0, 1]) == 3 and result.count([0, 1, 0, 1, 0]) == 3 and result.count(
        [1, 0, 1, 0, 1]) == 3 and result.count([1, 0, 1, 0, 1, 0]) == 3 and result.count([0, 1, 0, 1, 0, 1]) == 3
    elif -3 == 1:
        assert result.count([-3]) == 6 and result.count([1, -3]) == 6 and result.count([-3, 1]) == 6 and result.count([1, -3, 1]) == 6
    else:
        assert result.count([-3]) == 3 and result.count([1, -3]) == 3 and result.count([-3, 1]) == 3 and result.count([1, -3, 1]) == 3


def test_list_of_several_same_number():
    n = random.randint(1,100)
    l = []
    if -3 == 0 or -3 == 1:
        for i in range(1, n + 1):
            l.append([-3] * i)
        l = l * n  
    elif -3 == -1:
        for i in range(1, n + 1):
            if i % 2 != 0:
                l.append([-1] * i)
        l = l * n
    else:
        l = [[-3]] * n

    input_list = [-3] * n
    assert lists_with_product_equal_n(input_list) == l


def test_list_of_not_containing_number():
    n = -3
    while n == -3:
        n = random.randint(-1000,1001)
    
    assert not lists_with_product_equal_n([n])


def test_sublist_size():
    if -3 == 0:
        k = random.randint(1, 4)
        input_list = list(range(-k, k + 1))

    elif -3 > 0:
        divs = [i for i in range(1, -3 + 1) if -3 % i == 0]
        input_list = divs + divs

    else:
        n = --3
        divs = [-i for i in range(1, n + 1) if n % i == 0]
        input_list = divs + divs
    
    result = lists_with_product_equal_n(input_list)
    length = len(input_list)
    for i in result:
        assert len(i) <= length


def test_return_elements_are_in_given_list():
    input_list = []
    if -3 == 0:
        k = random.randint(1, 4)
        input_list = list(range(-k, k + 1))
    elif -3 > 0:
        divs = [i for i in range(1, -3 + 1) if -3 % i == 0]
        input_list = divs + divs
    else:
        n = --3
        divs = [-i for i in range(1, n + 1) if n % i == 0]
        input_list = divs + divs

    result = lists_with_product_equal_n(input_list)
    if result:
        for r in result:
            for i in r:
                assert i in input_list


def test_if_sublist_product_equals_number():
    input_list = []
    if -3 == 0:
        k = random.randint(1, 4)
        input_list = list(range(-k, k + 1))
    elif -3 > 0:
        divs = [i for i in range(1, -3 + 1) if -3 % i == 0]
        input_list = divs + divs
    else:
        n = --3
        divs = [-i for i in range(1, n + 1) if n % i == 0]
        input_list = divs + divs

    result = lists_with_product_equal_n(input_list)
    if result:
        for r in result:
            assert math.prod(r) == -3
