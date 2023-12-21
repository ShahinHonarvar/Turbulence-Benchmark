from Q28.gpt_3_5_turbo_results_1.Folder_91.generated_answer import return_nth_smallest_ascii
import random
import string



def test_result_is_in_given_string():
    s = ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation + ' ', k=93))
    assert return_nth_smallest_ascii(s) in s[0: 7 + 1]


def test_result_is_larger():
    s = ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation + ' ', k=93))
    s_copy = '' + s
    result = return_nth_smallest_ascii(s)
    s_copy = s_copy[0: 7 + 1]
    count = 0
    for char in s_copy:
        if result > char:
            count += 1
    assert count == 8 - 1


def test_result_is_smaller():
    s = ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation + ' ', k=93))
    s_copy = '' + s
    result = return_nth_smallest_ascii(s)
    s_copy = s_copy[0: 7 + 1]
    count = 0
    for char in s_copy:
        if result < char:
            count += 1
    assert count == len(s_copy) - 8


def test_random_string():
    s = ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation + ' ', k=93))
    output = return_nth_smallest_ascii(s)
    sliced_s = s[0:7 + 1]
    sorted_sliced_s = sorted(sliced_s)
    assert output == sorted_sliced_s[8 - 1]
    