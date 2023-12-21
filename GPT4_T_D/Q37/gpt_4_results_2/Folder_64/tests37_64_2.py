from Q37.gpt_4_results_2.Folder_64.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (7 + 2)
    if 'L' <= 'm' <= 'a':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(7 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[1:7+1]
    for char in sliced_s:
        if 'L' <= char <= 'a':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(7*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('L'), ord('a') + 1))
    for _ in range(7 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('L'), ord('a') + 1))
    for _ in range(1 + 1):
        s += 'L'
    for _ in range(7 - 1):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
