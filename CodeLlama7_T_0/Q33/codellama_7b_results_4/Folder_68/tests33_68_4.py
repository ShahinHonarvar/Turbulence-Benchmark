from Q33.codellama_7b_results_4.Folder_68.generated_answer import return_vowels
import string
import random


def test_repeat_consonant_char():
    s = 'm' * (9 + 2)
    assert not return_vowels(s)
   

def test_distinct_consonant_chars():
    s = 'BCDFGHJKLMNPQRSTVXZWYbcdfghjklmnpqrstvxzwy'
    assert not return_vowels(s)


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(9*100))
    assert len(return_vowels(s)) <= len(s)


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(9*2))
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    returned_s = return_vowels(s)
    sliced_s = s[1:9]
    for char in sliced_s:
        if char in vowels and '?' < char <= 'k':
            assert char in returned_s


def test_no_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(1)) + 'd' * (9-1) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))

    assert not return_vowels(s)


def test_all_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(1)) + 'i' * (9-1) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))
    
    if '?' < 'i' <= 'k':
        assert return_vowels(s) == ['i' for _ in range(9-1)]
    else:
        assert not return_vowels(s)
        