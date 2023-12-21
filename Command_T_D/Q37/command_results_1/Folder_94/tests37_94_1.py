from Q37.command_results_1.Folder_94.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (96 + 2)
    if 'X' <= 'm' <= 'p':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(96 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[51:96+1]
    for char in sliced_s:
        if 'X' <= char <= 'p':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(96*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('X'), ord('p') + 1))
    for _ in range(96 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('X'), ord('p') + 1))
    for _ in range(51 + 1):
        s += 'X'
    for _ in range(96 - 51):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
