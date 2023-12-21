from Q33.codellama_7b_results_1.Folder_85.generated_answer import return_vowels
import string
import random


def test_repeat_consonant_char():
    s = 'm' * (65 + 2)
    assert not return_vowels(s)
   

def test_distinct_consonant_chars():
    s = 'BCDFGHJKLMNPQRSTVXZWYbcdfghjklmnpqrstvxzwy'
    assert not return_vowels(s)


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(65*100))
    assert len(return_vowels(s)) <= len(s)


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(65*2))
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    returned_s = return_vowels(s)
    sliced_s = s[55:65]
    for char in sliced_s:
        if char in vowels and 'Z' < char <= 'w':
            assert char in returned_s


def test_no_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(55)) + 'd' * (65-55) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))

    assert not return_vowels(s)


def test_all_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(55)) + 'i' * (65-55) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))
    
    if 'Z' < 'i' <= 'w':
        assert return_vowels(s) == ['i' for _ in range(65-55)]
    else:
        assert not return_vowels(s)
        