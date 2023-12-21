from Q33.codellama_results_2.Folder_54.generated_answer import return_vowels
import string
import random


def test_repeat_consonant_char():
    s = 'm' * (85 + 2)
    assert not return_vowels(s)
   

def test_distinct_consonant_chars():
    s = 'BCDFGHJKLMNPQRSTVXZWYbcdfghjklmnpqrstvxzwy'
    assert not return_vowels(s)


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(85*100))
    assert len(return_vowels(s)) <= len(s)


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(85*2))
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    returned_s = return_vowels(s)
    sliced_s = s[23:85]
    for char in sliced_s:
        if char in vowels and 'W' < char <= 'v':
            assert char in returned_s


def test_no_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(23)) + 'd' * (85-23) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))

    assert not return_vowels(s)


def test_all_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(23)) + 'i' * (85-23) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))
    
    if 'W' < 'i' <= 'v':
        assert return_vowels(s) == ['i' for _ in range(85-23)]
    else:
        assert not return_vowels(s)
        