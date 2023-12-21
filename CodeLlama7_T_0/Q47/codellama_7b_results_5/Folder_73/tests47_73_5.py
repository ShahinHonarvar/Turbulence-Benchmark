from Q47.codellama_7b_results_5.Folder_73.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(62, 33)
    m = min(62 - 21 + 1, 33)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(22, m + 1)}


def test_string_of_similar_nums():
    n = max(62, 33)
    m = min(62 - 21 - 1, 33)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (62 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (62 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (62 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(62 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 22 <= len(i) <= 33


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(62 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[21: 62 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (62 * 3)
    assert not palindromes_of_specific_lengths(s)
    