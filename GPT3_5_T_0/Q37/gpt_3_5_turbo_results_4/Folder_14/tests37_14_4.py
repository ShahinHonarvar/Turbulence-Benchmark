from Q37.gpt_3_5_turbo_results_4.Folder_14.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (98 + 2)
    if 'A' <= 'm' <= 'b':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(98 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[35:98+1]
    for char in sliced_s:
        if 'A' <= char <= 'b':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(98*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('A'), ord('b') + 1))
    for _ in range(98 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('A'), ord('b') + 1))
    for _ in range(35 + 1):
        s += 'A'
    for _ in range(98 - 35):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
