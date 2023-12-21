from Q33.command_results_4.Folder_36.generated_answer import return_vowels
import string
import random


def test_repeat_consonant_char():
    s = 'm' * (949 + 2)
    assert not return_vowels(s)
   

def test_distinct_consonant_chars():
    s = 'BCDFGHJKLMNPQRSTVXZWYbcdfghjklmnpqrstvxzwy'
    assert not return_vowels(s)


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(949*100))
    assert len(return_vowels(s)) <= len(s)


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(949*2))
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    returned_s = return_vowels(s)
    sliced_s = s[604:949]
    for char in sliced_s:
        if char in vowels and 'N' < char <= 'U':
            assert char in returned_s


def test_no_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(604)) + 'd' * (949-604) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))

    assert not return_vowels(s)


def test_all_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(604)) + 'i' * (949-604) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))
    
    if 'N' < 'i' <= 'U':
        assert return_vowels(s) == ['i' for _ in range(949-604)]
    else:
        assert not return_vowels(s)
        