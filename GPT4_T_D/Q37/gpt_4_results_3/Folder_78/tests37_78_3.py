from Q37.gpt_4_results_3.Folder_78.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (99 + 2)
    if '8' <= 'm' <= 'e':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(99 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[75:99+1]
    for char in sliced_s:
        if '8' <= char <= 'e':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(99*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('8'), ord('e') + 1))
    for _ in range(99 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('8'), ord('e') + 1))
    for _ in range(75 + 1):
        s += '8'
    for _ in range(99 - 75):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
