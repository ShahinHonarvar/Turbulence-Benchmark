from Q47.codellama_results_1.Folder_18.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(83, 66)
    m = min(83 - 11 + 1, 66)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(13, m + 1)}


def test_string_of_similar_nums():
    n = max(83, 66)
    m = min(83 - 11 - 1, 66)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (83 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (83 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (83 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(83 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 13 <= len(i) <= 66


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(83 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[11: 83 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (83 * 3)
    assert not palindromes_of_specific_lengths(s)
    