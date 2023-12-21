from Q52.gpt_4_results_4.Folder_25.generated_answer import palindrome_of_length_n
import string
import random



def test_string_of_many_chars():
    s = 'abcdef'
    assert not palindrome_of_length_n(s)


def test_string_of_spaces():
    s = ' ' * (90 * 2)
    assert not palindrome_of_length_n(s)


def test_string_of_spaces_and_letters():
    s = 'a a' * (90 * 2)
    assert not palindrome_of_length_n(s)


def test_string_of_punctuations_and_letters():
    s = 'a&a' * (90 * 2)
    assert not palindrome_of_length_n(s)


def test_string_of_identical_nums():
    s = '0' * (90 * 2)
    assert not palindrome_of_length_n(s)


def test_string_of_numbers_and_letters():
    s = 'a1a' * (90 * 2)
    assert not palindrome_of_length_n(s)


def test_length_of_palindrome():
    n = random.randint(5, 10)
    s = 'a' * (90 * n)
    returned_result = palindrome_of_length_n(s)
    for i in returned_result:
        assert len(i) == 90


def test_length_less_than_90():
    s = ''.join('a' for _ in range(90 - 1))
    assert not palindrome_of_length_n(s)
    

def test_length_equal_to_90():
    s = 'a' * 90
    assert palindrome_of_length_n(s) == {s}


def test_string_of_identical_punctuations():
    s = '@' * (90 * 2)
    assert not palindrome_of_length_n(s)


def test_string_of_punctuations_and_nums():
    s = '1&' * (90 * 2)
    assert not palindrome_of_length_n(s)


def test_string_of_spaces_and_punctuations():
    s = '@ @' * (90 * 2)
    assert not palindrome_of_length_n(s)


def test_string_of_spaces_and_punctuations_nums_letters():
    s = '0 @ a a @ 0' * (90 * 2)
    assert not palindrome_of_length_n(s)
    