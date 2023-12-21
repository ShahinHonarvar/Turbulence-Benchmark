from Q33.command_results_5.Folder_65.generated_answer import return_vowels
import string
import random


def test_repeat_consonant_char():
    s = 'm' * (88 + 2)
    assert not return_vowels(s)
   

def test_distinct_consonant_chars():
    s = 'BCDFGHJKLMNPQRSTVXZWYbcdfghjklmnpqrstvxzwy'
    assert not return_vowels(s)


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(88*100))
    assert len(return_vowels(s)) <= len(s)


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(88*2))
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    returned_s = return_vowels(s)
    sliced_s = s[71:88]
    for char in sliced_s:
        if char in vowels and '9' < char <= 'P':
            assert char in returned_s


def test_no_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(71)) + 'd' * (88-71) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))

    assert not return_vowels(s)


def test_all_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(71)) + 'i' * (88-71) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))
    
    if '9' < 'i' <= 'P':
        assert return_vowels(s) == ['i' for _ in range(88-71)]
    else:
        assert not return_vowels(s)
        