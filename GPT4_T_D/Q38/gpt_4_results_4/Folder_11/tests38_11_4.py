from Q38.gpt_4_results_4.Folder_11.generated_answer import find_subset_of_length_n
import math
import random
import string


def test_smaller_sets():
    set_lengths = {i for i in range(1, 77)}
    for i in set_lengths:
        initial_set = {j for j in range(i)}
        assert find_subset_of_length_n(initial_set) == 0


def test_set_of_length_77_plus_1():
    initial_set = {i for i in range(77+1)}
    assert find_subset_of_length_n(initial_set) == 77+1 
        

def test_largest_subset():
    # This condition is used since the question says the
    # argument should be a set of elements, which means the
    # size of the argument should be greater than 1.
    if 77 >= 2:
        initial_set = {i for i in range(77)}
        assert find_subset_of_length_n(initial_set) == 1


def test_result_smaller_than_number_of_all_subsets():
    initial_set = {i for i in range(77 + 2)}
    number_of_all_subsets = pow(2, len(initial_set))
    assert find_subset_of_length_n(initial_set) < number_of_all_subsets


def test_set_of_strings():
    initial_set = set(string.printable)
    if 77 <= 100:
        assert find_subset_of_length_n(initial_set) == math.comb(len(initial_set), 77)
    else:
        assert find_subset_of_length_n(initial_set) == 0


def test_set_of_float_numbers():
    initial_set = set()
    while len(initial_set) < (77 + 1) + 100:
        initial_set.add(round(random.uniform(-100.0, 100.0),5))
    assert find_subset_of_length_n(initial_set) == math.comb(len(initial_set), 77)


def test_set_of_numbers_strings_bools():
    initial_set = set()
    while len(initial_set) < (77 + 1) + 100:
        initial_set.add(round(random.uniform(-100.0, 100.0),5))
    initial_set |= set(string.printable)
    initial_set |= {True,False}
    assert find_subset_of_length_n(initial_set) == math.comb(len(initial_set), 77)
    