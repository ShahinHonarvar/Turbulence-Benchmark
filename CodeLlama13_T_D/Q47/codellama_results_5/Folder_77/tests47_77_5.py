from Q47.codellama_results_5.Folder_77.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(276, 169)
    m = min(276 - 103 + 1, 169)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(100, m + 1)}


def test_string_of_similar_nums():
    n = max(276, 169)
    m = min(276 - 103 - 1, 169)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (276 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (276 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (276 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(276 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 100 <= len(i) <= 169


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(276 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[103: 276 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (276 * 3)
    assert not palindromes_of_specific_lengths(s)
    