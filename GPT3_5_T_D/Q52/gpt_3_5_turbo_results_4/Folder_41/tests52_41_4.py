from Q52.gpt_3_5_turbo_results_4.Folder_41.generated_answer import palindrome_of_length_n
import string
import random



def test_string_of_many_chars():
    s = 'abcdef'
    assert not palindrome_of_length_n(s)


def test_string_of_spaces():
    s = ' ' * (60 * 2)
    assert not palindrome_of_length_n(s)


def test_string_of_spaces_and_letters():
    s = 'a a' * (60 * 2)
    assert not palindrome_of_length_n(s)


def test_string_of_punctuations_and_letters():
    s = 'a&a' * (60 * 2)
    assert not palindrome_of_length_n(s)


def test_string_of_identical_nums():
    s = '0' * (60 * 2)
    assert not palindrome_of_length_n(s)


def test_string_of_numbers_and_letters():
    s = 'a1a' * (60 * 2)
    assert not palindrome_of_length_n(s)


def test_length_of_palindrome():
    n = random.randint(5, 10)
    s = 'a' * (60 * n)
    returned_result = palindrome_of_length_n(s)
    for i in returned_result:
        assert len(i) == 60


def test_length_less_than_60():
    s = ''.join('a' for _ in range(60 - 1))
    assert not palindrome_of_length_n(s)
    

def test_length_equal_to_60():
    s = 'a' * 60
    assert palindrome_of_length_n(s) == {s}


def test_string_of_identical_punctuations():
    s = '@' * (60 * 2)
    assert not palindrome_of_length_n(s)


def test_string_of_punctuations_and_nums():
    s = '1&' * (60 * 2)
    assert not palindrome_of_length_n(s)


def test_string_of_spaces_and_punctuations():
    s = '@ @' * (60 * 2)
    assert not palindrome_of_length_n(s)


def test_string_of_spaces_and_punctuations_nums_letters():
    s = '0 @ a a @ 0' * (60 * 2)
    assert not palindrome_of_length_n(s)
    