from Q47.codellama_7b_results_2.Folder_80.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(88, 33)
    m = min(88 - 35 + 1, 33)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(24, m + 1)}


def test_string_of_similar_nums():
    n = max(88, 33)
    m = min(88 - 35 - 1, 33)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (88 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (88 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (88 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(88 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 24 <= len(i) <= 33


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(88 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[35: 88 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (88 * 3)
    assert not palindromes_of_specific_lengths(s)
    