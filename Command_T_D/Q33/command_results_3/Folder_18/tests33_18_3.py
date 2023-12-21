from Q33.command_results_3.Folder_18.generated_answer import return_vowels
import string
import random


def test_repeat_consonant_char():
    s = 'm' * (606 + 2)
    assert not return_vowels(s)
   

def test_distinct_consonant_chars():
    s = 'BCDFGHJKLMNPQRSTVXZWYbcdfghjklmnpqrstvxzwy'
    assert not return_vowels(s)


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(606*100))
    assert len(return_vowels(s)) <= len(s)


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(606*2))
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    returned_s = return_vowels(s)
    sliced_s = s[528:606]
    for char in sliced_s:
        if char in vowels and 'M' < char <= 'X':
            assert char in returned_s


def test_no_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(528)) + 'd' * (606-528) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))

    assert not return_vowels(s)


def test_all_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(528)) + 'i' * (606-528) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))
    
    if 'M' < 'i' <= 'X':
        assert return_vowels(s) == ['i' for _ in range(606-528)]
    else:
        assert not return_vowels(s)
        