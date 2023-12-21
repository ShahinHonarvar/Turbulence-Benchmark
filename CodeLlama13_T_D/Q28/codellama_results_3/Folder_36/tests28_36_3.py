from Q28.codellama_results_3.Folder_36.generated_answer import return_nth_smallest_ascii
import random
import string



def test_result_is_in_given_string():
    s = ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation + ' ', k=93))
    assert return_nth_smallest_ascii(s) in s[17: 56 + 1]


def test_result_is_larger():
    s = ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation + ' ', k=93))
    s_copy = '' + s
    result = return_nth_smallest_ascii(s)
    s_copy = s_copy[17: 56 + 1]
    count = 0
    for char in s_copy:
        if result > char:
            count += 1
    assert count == 9 - 1


def test_result_is_smaller():
    s = ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation + ' ', k=93))
    s_copy = '' + s
    result = return_nth_smallest_ascii(s)
    s_copy = s_copy[17: 56 + 1]
    count = 0
    for char in s_copy:
        if result < char:
            count += 1
    assert count == len(s_copy) - 9


def test_random_string():
    s = ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation + ' ', k=93))
    output = return_nth_smallest_ascii(s)
    sliced_s = s[17:56 + 1]
    sorted_sliced_s = sorted(sliced_s)
    assert output == sorted_sliced_s[9 - 1]
    