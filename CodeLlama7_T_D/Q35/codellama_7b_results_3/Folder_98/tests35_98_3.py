from Q35.codellama_7b_results_3.Folder_98.generated_answer import remove_repeat_chars
import string
import random


def test_repeat_char():
    s = 'a' * (7 + 2)
    if 7 - 0 - 1 == 1:
        assert remove_repeat_chars(s) == s
    else:
        assert not remove_repeat_chars(s)


def test_no_duplicate_string():
    s = 'abcdefghijklmnopqrstuvwxyz 0123456789'
    assert remove_repeat_chars(s) == s


def test_merged_strings():
    s = ('a' * (7 + 1)) + ('b' * 7)
    if 7 - 0 - 1 == 1:
        assert remove_repeat_chars(s) == s
    else:
        assert remove_repeat_chars(s) == 'b' * 7


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(7*100))
    assert len(remove_repeat_chars(s)) <= len(s)


def test_absence_of_duplicates():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(7*2))
    sliced_s = s[0 + 1:7]
    returned_s = remove_repeat_chars(s)
    for char in s:
        if sliced_s.count(char) > 1:
            assert char not in returned_s


def test_presence_of_non_duplicates():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(7*2))
    returned_s = remove_repeat_chars(s)
    for char in s:
        if s.count(char) == 1:
            assert char in returned_s


def test_presence_of_duplicates_not_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(7*2))
    sliced_s = s[0 + 1:7]
    returned_s = remove_repeat_chars(s)
    for char in s:
        if s.count(char) > 1 and char not in sliced_s:
            assert s.count(char) == returned_s.count(char)
