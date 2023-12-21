from Q56.codellama_7b_results_2.Folder_98.generated_answer import all_substring_of_size_n
import random
import string


def test_string_of_same_character():
    selection = [' ', '0', '@', 'a']
    for char in selection:
        s = ''.join(char for _ in range(1, 10 + 10))
        assert not all_substring_of_size_n(s)


def test_one_character_string():
    # Since the parameter generater (i.e. genparams.py) generates only parameters
    # of equal to or greater than 2, the answer should be an empty list.
    assert not all_substring_of_size_n('a')


def test_same_character_string():
    s = 'a' * 10
    assert not all_substring_of_size_n(s)


def test_large_string():
    if 10 < 63:
        s = ''.join(random.sample(string.ascii_letters + string.digits, k=10))
        assert all_substring_of_size_n(s) == [s]
    else:
        s = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        assert not all_substring_of_size_n(s)


def test_length_of_substring_result():
    if 10 < 50:
        s = ''.join(random.sample(string.ascii_letters + string.digits, k=10 + 10))
    else:
        s = ''.join(random.choices(string.ascii_letters + string.digits, k=10 + 10))
    
    output = all_substring_of_size_n(s)
    for i in output:
        assert len(i) <= len(s)