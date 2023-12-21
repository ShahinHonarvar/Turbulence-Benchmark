from Q37.codellama_7b_results_3.Folder_51.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (40 + 2)
    if 'H' <= 'm' <= 'e':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(40 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[36:40+1]
    for char in sliced_s:
        if 'H' <= char <= 'e':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(40*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('H'), ord('e') + 1))
    for _ in range(40 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('H'), ord('e') + 1))
    for _ in range(36 + 1):
        s += 'H'
    for _ in range(40 - 36):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
