from Q37.gpt_3_5_turbo_results_3.Folder_40.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (1 + 2)
    if '*' <= 'm' <= 's':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(1 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[0:1+1]
    for char in sliced_s:
        if '*' <= char <= 's':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(1*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('*'), ord('s') + 1))
    for _ in range(1 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('*'), ord('s') + 1))
    for _ in range(0 + 1):
        s += '*'
    for _ in range(1 - 0):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
