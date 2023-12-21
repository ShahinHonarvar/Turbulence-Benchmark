from Q37.gpt_3_5_turbo_results_2.Folder_88.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (80 + 2)
    if '@' <= 'm' <= 'p':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(80 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[69:80+1]
    for char in sliced_s:
        if '@' <= char <= 'p':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(80*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('@'), ord('p') + 1))
    for _ in range(80 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('@'), ord('p') + 1))
    for _ in range(69 + 1):
        s += '@'
    for _ in range(80 - 69):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
