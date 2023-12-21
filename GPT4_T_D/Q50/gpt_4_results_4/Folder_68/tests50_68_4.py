from Q50.gpt_4_results_4.Folder_68.generated_answer import if_contains_anagrams
import random
import itertools



def test_list_of_strings_of_length_two():
    l = ['aa', 'aa'] * (9 + 1)
    assert not if_contains_anagrams(l)


def test_list_of_two_strings_of_different_lengths():
    l = ['aaa', 'aaaa']
    assert not if_contains_anagrams(l)


def test_list_of_many_strings_with_different_lengths():
    l = ['a' * i for i in range(3, 101)]
    assert not if_contains_anagrams(l)


def test_list_of_anagrams_of_size_n():
    d = {3:'aBc', 4:'AbCd', 5:'aBCdE', 6:'AbCdEf'}
    for i in range(3,7):
        l = [''.join(j) for j in itertools.permutations(d[i])]
        if i == 3:
            if 9 < 16:
                assert if_contains_anagrams(l)
            else:
                assert not if_contains_anagrams(l)
        elif i == 4:
            if 9 < 277:
               assert if_contains_anagrams(l)
            else:
               assert not if_contains_anagrams(l)
        else:
            assert if_contains_anagrams(l)


def test_list_of_strings_including_one_same_uppercase_char_1():
    s = 'a' * 50
    l = [s[:i] + 'A' + s[i+1:] for i in range(len(s))]
    assert if_contains_anagrams(l)


def test_list_of_strings_including_one_same_uppercase_char_2():
    s = 'a' * 6
    l = [s[:i] + 'A' + s[i+1:] for i in range(len(s))]
    if 9 < 16:
        assert if_contains_anagrams(l)
    else:
        assert not if_contains_anagrams(l)


def test_list_of_strings_including_one_same_lowercase_char_1():
    s = 'A' * 50
    l = [s[:i] + 'a' + s[i+1:] for i in range(len(s))]
    assert if_contains_anagrams(l)


def test_list_of_strings_including_one_same_lowercase_char_2():
    s = 'A' * 6
    l = [s[:i] + 'a' + s[i+1:] for i in range(len(s))]
    if 9 < 16:
        assert if_contains_anagrams(l)
    else:
        assert not if_contains_anagrams(l)


def test_list_of_strings_including_one_distinct_sequence_1():
    s = 'A' * 50
    l = [s[:i] + 'test' + s[i+1:] for i in range(len(s))]
    assert if_contains_anagrams(l)


def test_list_of_strings_including_one_distinct_sequence_2():
    s = 'A' * 6
    l = [s[:i] + 'test' + s[i+1:] for i in range(len(s))]
    if 9 < 16:
        assert if_contains_anagrams(l)
    else:
        assert not if_contains_anagrams(l)
