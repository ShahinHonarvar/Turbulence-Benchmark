from Q33.codellama_results_3.Folder_48.generated_answer import return_vowels
import string
import random


def test_repeat_consonant_char():
    s = 'm' * (828 + 2)
    assert not return_vowels(s)
   

def test_distinct_consonant_chars():
    s = 'BCDFGHJKLMNPQRSTVXZWYbcdfghjklmnpqrstvxzwy'
    assert not return_vowels(s)


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(828*100))
    assert len(return_vowels(s)) <= len(s)


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(828*2))
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    returned_s = return_vowels(s)
    sliced_s = s[529:828]
    for char in sliced_s:
        if char in vowels and 'U' < char <= 'l':
            assert char in returned_s


def test_no_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(529)) + 'd' * (828-529) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))

    assert not return_vowels(s)


def test_all_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(529)) + 'i' * (828-529) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))
    
    if 'U' < 'i' <= 'l':
        assert return_vowels(s) == ['i' for _ in range(828-529)]
    else:
        assert not return_vowels(s)
        