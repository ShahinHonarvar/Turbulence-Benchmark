from Q37.codellama_7b_results_5.Folder_61.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (6 + 2)
    if 'G' <= 'm' <= 'p':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(6 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[5:6+1]
    for char in sliced_s:
        if 'G' <= char <= 'p':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(6*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('G'), ord('p') + 1))
    for _ in range(6 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('G'), ord('p') + 1))
    for _ in range(5 + 1):
        s += 'G'
    for _ in range(6 - 5):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
