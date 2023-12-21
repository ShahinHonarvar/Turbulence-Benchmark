from Q36.codellama_results_4.Folder_44.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (64 + 2)
    if '3' < 'm' < 'B':
        assert not filter_chars(s)
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(64 * 2))
    sliced_s = set(s[18 + 1:64])
    c = 0
    for char in sliced_s:
        if '3' < char < 'B':
            c += s.count(char)

    assert len(filter_chars(s)) == len(s) - c


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(64*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    given_range = list(range(ord('3') + 1, ord('B')))
    s = ''
    for _ in range(64 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ' + string.digits)
        while ord(char) in given_range:
            char = random.choice(string.ascii_letters + '$ % & * + < = > @ ' + string.digits)
        s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    for _ in range(64 + 10):
        char = random.randint(ord('3') + 1, ord('B')-1)
        s += chr(char)

    sliced_s = s[18 + 1:64]
    result = filter_chars(s)
    for char in sliced_s:
        assert char not in result
