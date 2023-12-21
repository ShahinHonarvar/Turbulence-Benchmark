from Q36.gpt_3_5_turbo_results_3.Folder_60.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (83 + 2)
    if 'f' < 'm' < 'o':
        assert not filter_chars(s)
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(83 * 2))
    sliced_s = set(s[23 + 1:83])
    c = 0
    for char in sliced_s:
        if 'f' < char < 'o':
            c += s.count(char)

    assert len(filter_chars(s)) == len(s) - c


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(83*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    given_range = list(range(ord('f') + 1, ord('o')))
    s = ''
    for _ in range(83 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ' + string.digits)
        while ord(char) in given_range:
            char = random.choice(string.ascii_letters + '$ % & * + < = > @ ' + string.digits)
        s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    for _ in range(83 + 10):
        char = random.randint(ord('f') + 1, ord('o')-1)
        s += chr(char)

    sliced_s = s[23 + 1:83]
    result = filter_chars(s)
    for char in sliced_s:
        assert char not in result
