from Q37.command_results_5.Folder_36.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (502 + 2)
    if ',' <= 'm' <= '3':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(502 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[259:502+1]
    for char in sliced_s:
        if ',' <= char <= '3':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(502*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord(','), ord('3') + 1))
    for _ in range(502 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord(','), ord('3') + 1))
    for _ in range(259 + 1):
        s += ','
    for _ in range(502 - 259):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
