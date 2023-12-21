from Q36.codellama_results_5.Folder_87.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (61 + 2)
    if '3' < 'm' < 'D':
        assert not filter_chars(s)
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(61 * 2))
    sliced_s = set(s[32 + 1:61])
    c = 0
    for char in sliced_s:
        if '3' < char < 'D':
            c += s.count(char)

    assert len(filter_chars(s)) == len(s) - c


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(61*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    given_range = list(range(ord('3') + 1, ord('D')))
    s = ''
    for _ in range(61 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ' + string.digits)
        while ord(char) in given_range:
            char = random.choice(string.ascii_letters + '$ % & * + < = > @ ' + string.digits)
        s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    for _ in range(61 + 10):
        char = random.randint(ord('3') + 1, ord('D')-1)
        s += chr(char)

    sliced_s = s[32 + 1:61]
    result = filter_chars(s)
    for char in sliced_s:
        assert char not in result
