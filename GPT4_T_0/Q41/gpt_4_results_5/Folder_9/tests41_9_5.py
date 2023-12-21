from Q41.gpt_4_results_5.Folder_9.generated_answer import identical_elements


def test_both_lists_empty():
    assert identical_elements([], []) = set()
    

def test_same_lists():
    first_list = [i for i in range(1, 200 * 10)]
    second_list = [i for i in range(1, 200 * 10)]
    assert identical_elements(first_list, second_list) == set(first_list[70:200 + 1])


def test_distinct_lists():
    positive_integers = [i for i in range(1, 200 * 10)]
    negative_integers = [-i for i in range(1, 200 * 10)]
    assert identical_elements(positive_integers, negative_integers) == set()


def test_one_element_in_common():
    positive_integers = [i for i in range(1, 200 * 10)]
    positive_integers.insert(70, 'a') 
    negative_integers = [-i for i in range(1, 200 * 10)]
    negative_integers.insert(200, 'a') 
    assert identical_elements(positive_integers, negative_integers) == {'a'}


def test_elements_in_common_out_of_given_range():
    positive_integers = [i for i in range(1, 200 * 10)]
    positive_integers.extend(['a', 'b', 'c', 'd', 'e'])
    negative_integers = [-i for i in range(1, 200 * 10)]
    negative_integers.extend(['a', 'b', 'c', 'd', 'e'])
    assert identical_elements(positive_integers, negative_integers) == set()


def test_zeros_and_ones():
    zeros = [0 for i in range(1, 200 * 2)]
    ones = [1 for i in range(1, 200 * 2)]
    assert identical_elements(zeros, ones) == set()


def test_list_of_empty_strings():
    empty_strings = ['' for _ in range(1, 200 * 2)]
    assert identical_elements(empty_strings, empty_strings) == set(empty_strings[70:200 + 1])


def test_nums_and_strings():
    nums = [i for i in range(1, 200 * 2)]
    strings = ['testing' for i in range(1, 200 * 2)]
    assert identical_elements(nums, strings) == set()


def test_nums_and_bools_1():
    nums = [0 if i % 2 == 0 else 1 for i in range(0, 200 * 2)]
    bools = [False if i % 2 == 0 else True for i in range(0, 200 * 2)]
    assert identical_elements(nums, bools) == set(nums[70:200 + 1])


def test_nums_and_bools_2():
    nums = [i for i in range(1, 200 * 2)]
    bools = [False for _ in range(1, 200 * 2)]
    assert identical_elements(nums, bools) == set()
    