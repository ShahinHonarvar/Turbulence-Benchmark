from Q37.codellama_7b_results_3.Folder_5.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (82 + 2)
    if '5' <= 'm' <= '<':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(82 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[24:82+1]
    for char in sliced_s:
        if '5' <= char <= '<':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(82*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('5'), ord('<') + 1))
    for _ in range(82 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('5'), ord('<') + 1))
    for _ in range(24 + 1):
        s += '5'
    for _ in range(82 - 24):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
