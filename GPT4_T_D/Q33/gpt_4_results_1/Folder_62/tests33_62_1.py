from Q33.gpt_4_results_1.Folder_62.generated_answer import return_vowels
import string
import random


def test_repeat_consonant_char():
    s = 'm' * (60 + 2)
    assert not return_vowels(s)
   

def test_distinct_consonant_chars():
    s = 'BCDFGHJKLMNPQRSTVXZWYbcdfghjklmnpqrstvxzwy'
    assert not return_vowels(s)


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(60*100))
    assert len(return_vowels(s)) <= len(s)


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(60*2))
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    returned_s = return_vowels(s)
    sliced_s = s[14:60]
    for char in sliced_s:
        if char in vowels and 'D' < char <= 'v':
            assert char in returned_s


def test_no_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(14)) + 'd' * (60-14) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))

    assert not return_vowels(s)


def test_all_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(14)) + 'i' * (60-14) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))
    
    if 'D' < 'i' <= 'v':
        assert return_vowels(s) == ['i' for _ in range(60-14)]
    else:
        assert not return_vowels(s)
        