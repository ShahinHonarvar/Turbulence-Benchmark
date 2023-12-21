from Q37.gpt_3_5_turbo_results_4.Folder_42.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (74 + 2)
    if 'U' <= 'm' <= 'l':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(74 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[73:74+1]
    for char in sliced_s:
        if 'U' <= char <= 'l':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(74*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('U'), ord('l') + 1))
    for _ in range(74 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('U'), ord('l') + 1))
    for _ in range(73 + 1):
        s += 'U'
    for _ in range(74 - 73):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
