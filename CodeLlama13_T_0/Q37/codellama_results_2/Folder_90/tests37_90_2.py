from Q37.codellama_results_2.Folder_90.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (852 + 2)
    if 'J' <= 'm' <= 'b':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(852 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[348:852+1]
    for char in sliced_s:
        if 'J' <= char <= 'b':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(852*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('J'), ord('b') + 1))
    for _ in range(852 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('J'), ord('b') + 1))
    for _ in range(348 + 1):
        s += 'J'
    for _ in range(852 - 348):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
