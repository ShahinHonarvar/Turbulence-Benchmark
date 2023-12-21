from Q36.gpt_4_results_5.Folder_65.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (82 + 2)
    if 'F' < 'm' < 'O':
        assert not filter_chars(s)
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(82 * 2))
    sliced_s = set(s[58 + 1:82])
    c = 0
    for char in sliced_s:
        if 'F' < char < 'O':
            c += s.count(char)

    assert len(filter_chars(s)) == len(s) - c


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(82*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    given_range = list(range(ord('F') + 1, ord('O')))
    s = ''
    for _ in range(82 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ' + string.digits)
        while ord(char) in given_range:
            char = random.choice(string.ascii_letters + '$ % & * + < = > @ ' + string.digits)
        s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    for _ in range(82 + 10):
        char = random.randint(ord('F') + 1, ord('O')-1)
        s += chr(char)

    sliced_s = s[58 + 1:82]
    result = filter_chars(s)
    for char in sliced_s:
        assert char not in result
