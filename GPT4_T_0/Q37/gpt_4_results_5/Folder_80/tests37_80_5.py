from Q37.gpt_4_results_5.Folder_80.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (79 + 2)
    if 'a' <= 'm' <= 'i':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(79 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[36:79+1]
    for char in sliced_s:
        if 'a' <= char <= 'i':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(79*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('a'), ord('i') + 1))
    for _ in range(79 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('a'), ord('i') + 1))
    for _ in range(36 + 1):
        s += 'a'
    for _ in range(79 - 36):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
