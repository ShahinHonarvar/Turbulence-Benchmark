from Q33.gpt_3_5_turbo_results_1.Folder_41.generated_answer import return_vowels
import string
import random


def test_repeat_consonant_char():
    s = 'm' * (81 + 2)
    assert not return_vowels(s)
   

def test_distinct_consonant_chars():
    s = 'BCDFGHJKLMNPQRSTVXZWYbcdfghjklmnpqrstvxzwy'
    assert not return_vowels(s)


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(81*100))
    assert len(return_vowels(s)) <= len(s)


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(81*2))
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    returned_s = return_vowels(s)
    sliced_s = s[71:81]
    for char in sliced_s:
        if char in vowels and '>' < char <= 'U':
            assert char in returned_s


def test_no_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(71)) + 'd' * (81-71) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))

    assert not return_vowels(s)


def test_all_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(71)) + 'i' * (81-71) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))
    
    if '>' < 'i' <= 'U':
        assert return_vowels(s) == ['i' for _ in range(81-71)]
    else:
        assert not return_vowels(s)
        