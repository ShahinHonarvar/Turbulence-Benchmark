from Q37.codellama_7b_results_4.Folder_76.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (898 + 2)
    if 'M' <= 'm' <= 'v':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(898 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[379:898+1]
    for char in sliced_s:
        if 'M' <= char <= 'v':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(898*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('M'), ord('v') + 1))
    for _ in range(898 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('M'), ord('v') + 1))
    for _ in range(379 + 1):
        s += 'M'
    for _ in range(898 - 379):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
