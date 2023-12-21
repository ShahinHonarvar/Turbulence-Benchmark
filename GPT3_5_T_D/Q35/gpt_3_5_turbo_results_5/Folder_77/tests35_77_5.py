from Q35.gpt_3_5_turbo_results_5.Folder_77.generated_answer import remove_repeat_chars
import string
import random


def test_repeat_char():
    s = 'a' * (988 + 2)
    if 988 - 355 - 1 == 1:
        assert remove_repeat_chars(s) == s
    else:
        assert not remove_repeat_chars(s)


def test_no_duplicate_string():
    s = 'abcdefghijklmnopqrstuvwxyz 0123456789'
    assert remove_repeat_chars(s) == s


def test_merged_strings():
    s = ('a' * (988 + 1)) + ('b' * 988)
    if 988 - 355 - 1 == 1:
        assert remove_repeat_chars(s) == s
    else:
        assert remove_repeat_chars(s) == 'b' * 988


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(988*100))
    assert len(remove_repeat_chars(s)) <= len(s)


def test_absence_of_duplicates():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(988*2))
    sliced_s = s[355 + 1:988]
    returned_s = remove_repeat_chars(s)
    for char in s:
        if sliced_s.count(char) > 1:
            assert char not in returned_s


def test_presence_of_non_duplicates():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(988*2))
    returned_s = remove_repeat_chars(s)
    for char in s:
        if s.count(char) == 1:
            assert char in returned_s


def test_presence_of_duplicates_not_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(988*2))
    sliced_s = s[355 + 1:988]
    returned_s = remove_repeat_chars(s)
    for char in s:
        if s.count(char) > 1 and char not in sliced_s:
            assert s.count(char) == returned_s.count(char)
