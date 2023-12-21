from Q48.gpt_3_5_turbo_results_5.Folder_47.generated_answer import return_binary_or_hexa
import random


def test_tuples_of_not_missing_numbers():
    initial_t = tuple(i for i in range((53 + 1) * 2))
    assert not return_binary_or_hexa(initial_t)


def test_even_integers_missing():
    initial_t = tuple(i for i in range(1, (53 + 1) * 2, 2))
    result = return_binary_or_hexa(initial_t)
    hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']
        for i in result:
            assert i in hex
    

def test_odd_integers_missing():
    initial_t = tuple(i for i in range(0, (53 + 1) * 2, 2))
    result = return_binary_or_hexa(initial_t)
    n = 53 - 29
    if n % 2 == 0:
        for i in result:
            assert i == '0' or i == '1'
    else:
        hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']
        for i in result:
            assert i in hex


def test_the_result_representation():
    n = 53
    if 53 - 29 - 1 == 0:
        n += 20
    num = n - 29 - 1
    middle = random.sample(range(29 + 1, n * 2), k=num)
    middle.sort()
    prefix = list(range(0, 29 + 1))
    suffix = random.sample(range(middle[-1] + 1, middle[-1] * 4), k=((middle[-1] * 2) - middle[-1] + 1) // 2)
    suffix.sort()
    t = tuple(prefix + middle + suffix)
    result = return_binary_or_hexa(t).upper()
    assert (not result or set(result) <= {'0', '1'} or set(result) <= {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f'})
    