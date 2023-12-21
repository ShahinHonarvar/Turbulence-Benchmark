from Q47.gpt_4_results_4.Folder_75.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(74, 39)
    m = min(74 - 31 + 1, 39)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(23, m + 1)}


def test_string_of_similar_nums():
    n = max(74, 39)
    m = min(74 - 31 - 1, 39)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (74 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (74 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (74 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(74 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 23 <= len(i) <= 39


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(74 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[31: 74 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (74 * 3)
    assert not palindromes_of_specific_lengths(s)
    