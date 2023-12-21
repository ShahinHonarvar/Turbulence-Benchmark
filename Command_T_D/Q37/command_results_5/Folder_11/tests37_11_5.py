from Q37.command_results_5.Folder_11.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (97 + 2)
    if '-' <= 'm' <= 'n':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(97 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[29:97+1]
    for char in sliced_s:
        if '-' <= char <= 'n':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(97*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('-'), ord('n') + 1))
    for _ in range(97 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('-'), ord('n') + 1))
    for _ in range(29 + 1):
        s += '-'
    for _ in range(97 - 29):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
