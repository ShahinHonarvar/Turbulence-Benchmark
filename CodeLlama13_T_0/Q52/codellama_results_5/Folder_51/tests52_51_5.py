from Q52.codellama_results_5.Folder_51.generated_answer import palindrome_of_length_n
import string
import random



def test_string_of_many_chars():
    s = 'abcdef'
    assert not palindrome_of_length_n(s)


def test_string_of_spaces():
    s = ' ' * (73 * 2)
    assert not palindrome_of_length_n(s)


def test_string_of_spaces_and_letters():
    s = 'a a' * (73 * 2)
    assert not palindrome_of_length_n(s)


def test_string_of_punctuations_and_letters():
    s = 'a&a' * (73 * 2)
    assert not palindrome_of_length_n(s)


def test_string_of_identical_nums():
    s = '0' * (73 * 2)
    assert not palindrome_of_length_n(s)


def test_string_of_numbers_and_letters():
    s = 'a1a' * (73 * 2)
    assert not palindrome_of_length_n(s)


def test_length_of_palindrome():
    n = random.randint(5, 10)
    s = 'a' * (73 * n)
    returned_result = palindrome_of_length_n(s)
    for i in returned_result:
        assert len(i) == 73


def test_length_less_than_73():
    s = ''.join('a' for _ in range(73 - 1))
    assert not palindrome_of_length_n(s)
    

def test_length_equal_to_73():
    s = 'a' * 73
    assert palindrome_of_length_n(s) == {s}


def test_string_of_identical_punctuations():
    s = '@' * (73 * 2)
    assert not palindrome_of_length_n(s)


def test_string_of_punctuations_and_nums():
    s = '1&' * (73 * 2)
    assert not palindrome_of_length_n(s)


def test_string_of_spaces_and_punctuations():
    s = '@ @' * (73 * 2)
    assert not palindrome_of_length_n(s)


def test_string_of_spaces_and_punctuations_nums_letters():
    s = '0 @ a a @ 0' * (73 * 2)
    assert not palindrome_of_length_n(s)
    