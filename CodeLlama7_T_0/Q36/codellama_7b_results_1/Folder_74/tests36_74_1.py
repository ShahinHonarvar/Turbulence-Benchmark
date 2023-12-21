from Q36.codellama_7b_results_1.Folder_74.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (36 + 2)
    if '>' < 'm' < 'A':
        assert not filter_chars(s)
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(36 * 2))
    sliced_s = set(s[33 + 1:36])
    c = 0
    for char in sliced_s:
        if '>' < char < 'A':
            c += s.count(char)

    assert len(filter_chars(s)) == len(s) - c


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(36*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    given_range = list(range(ord('>') + 1, ord('A')))
    s = ''
    for _ in range(36 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ' + string.digits)
        while ord(char) in given_range:
            char = random.choice(string.ascii_letters + '$ % & * + < = > @ ' + string.digits)
        s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    for _ in range(36 + 10):
        char = random.randint(ord('>') + 1, ord('A')-1)
        s += chr(char)

    sliced_s = s[33 + 1:36]
    result = filter_chars(s)
    for char in sliced_s:
        assert char not in result
