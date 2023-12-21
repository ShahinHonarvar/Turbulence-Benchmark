from Q37.codellama_results_2.Folder_22.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (70 + 2)
    if '7' <= 'm' <= 'k':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(70 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[33:70+1]
    for char in sliced_s:
        if '7' <= char <= 'k':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(70*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('7'), ord('k') + 1))
    for _ in range(70 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('7'), ord('k') + 1))
    for _ in range(33 + 1):
        s += '7'
    for _ in range(70 - 33):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
