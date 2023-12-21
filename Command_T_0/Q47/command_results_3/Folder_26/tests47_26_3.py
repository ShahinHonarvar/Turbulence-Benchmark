from Q47.command_results_3.Folder_26.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(84, 31)
    m = min(84 - 24 + 1, 31)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(21, m + 1)}


def test_string_of_similar_nums():
    n = max(84, 31)
    m = min(84 - 24 - 1, 31)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (84 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (84 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (84 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(84 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 21 <= len(i) <= 31


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(84 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[24: 84 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (84 * 3)
    assert not palindromes_of_specific_lengths(s)
    