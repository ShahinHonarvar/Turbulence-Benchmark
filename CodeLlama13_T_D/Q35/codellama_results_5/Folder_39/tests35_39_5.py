from Q35.codellama_results_5.Folder_39.generated_answer import remove_repeat_chars
import string
import random


def test_repeat_char():
    s = 'a' * (91 + 2)
    if 91 - 44 - 1 == 1:
        assert remove_repeat_chars(s) == s
    else:
        assert not remove_repeat_chars(s)


def test_no_duplicate_string():
    s = 'abcdefghijklmnopqrstuvwxyz 0123456789'
    assert remove_repeat_chars(s) == s


def test_merged_strings():
    s = ('a' * (91 + 1)) + ('b' * 91)
    if 91 - 44 - 1 == 1:
        assert remove_repeat_chars(s) == s
    else:
        assert remove_repeat_chars(s) == 'b' * 91


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(91*100))
    assert len(remove_repeat_chars(s)) <= len(s)


def test_absence_of_duplicates():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(91*2))
    sliced_s = s[44 + 1:91]
    returned_s = remove_repeat_chars(s)
    for char in s:
        if sliced_s.count(char) > 1:
            assert char not in returned_s


def test_presence_of_non_duplicates():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(91*2))
    returned_s = remove_repeat_chars(s)
    for char in s:
        if s.count(char) == 1:
            assert char in returned_s


def test_presence_of_duplicates_not_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(91*2))
    sliced_s = s[44 + 1:91]
    returned_s = remove_repeat_chars(s)
    for char in s:
        if s.count(char) > 1 and char not in sliced_s:
            assert s.count(char) == returned_s.count(char)
