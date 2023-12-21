from Q37.codellama_7b_results_4.Folder_19.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (89 + 2)
    if 'E' <= 'm' <= 't':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(89 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[35:89+1]
    for char in sliced_s:
        if 'E' <= char <= 't':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(89*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('E'), ord('t') + 1))
    for _ in range(89 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('E'), ord('t') + 1))
    for _ in range(35 + 1):
        s += 'E'
    for _ in range(89 - 35):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
