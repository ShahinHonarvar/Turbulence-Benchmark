from Q37.command_results_2.Folder_98.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (9 + 2)
    if 'R' <= 'm' <= 't':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(9 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[8:9+1]
    for char in sliced_s:
        if 'R' <= char <= 't':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(9*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('R'), ord('t') + 1))
    for _ in range(9 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('R'), ord('t') + 1))
    for _ in range(8 + 1):
        s += 'R'
    for _ in range(9 - 8):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
