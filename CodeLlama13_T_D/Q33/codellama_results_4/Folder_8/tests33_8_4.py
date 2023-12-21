from Q33.codellama_results_4.Folder_8.generated_answer import return_vowels
import string
import random


def test_repeat_consonant_char():
    s = 'm' * (82 + 2)
    assert not return_vowels(s)
   

def test_distinct_consonant_chars():
    s = 'BCDFGHJKLMNPQRSTVXZWYbcdfghjklmnpqrstvxzwy'
    assert not return_vowels(s)


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(82*100))
    assert len(return_vowels(s)) <= len(s)


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(82*2))
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    returned_s = return_vowels(s)
    sliced_s = s[64:82]
    for char in sliced_s:
        if char in vowels and 'P' < char <= 'z':
            assert char in returned_s


def test_no_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(64)) + 'd' * (82-64) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))

    assert not return_vowels(s)


def test_all_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(64)) + 'i' * (82-64) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))
    
    if 'P' < 'i' <= 'z':
        assert return_vowels(s) == ['i' for _ in range(82-64)]
    else:
        assert not return_vowels(s)
        