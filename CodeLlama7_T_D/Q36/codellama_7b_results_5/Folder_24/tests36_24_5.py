from Q36.codellama_7b_results_5.Folder_24.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (15 + 2)
    if 't' < 'm' < 'v':
        assert not filter_chars(s)
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(15 * 2))
    sliced_s = set(s[10 + 1:15])
    c = 0
    for char in sliced_s:
        if 't' < char < 'v':
            c += s.count(char)

    assert len(filter_chars(s)) == len(s) - c


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(15*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    given_range = list(range(ord('t') + 1, ord('v')))
    s = ''
    for _ in range(15 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ' + string.digits)
        while ord(char) in given_range:
            char = random.choice(string.ascii_letters + '$ % & * + < = > @ ' + string.digits)
        s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    for _ in range(15 + 10):
        char = random.randint(ord('t') + 1, ord('v')-1)
        s += chr(char)

    sliced_s = s[10 + 1:15]
    result = filter_chars(s)
    for char in sliced_s:
        assert char not in result
