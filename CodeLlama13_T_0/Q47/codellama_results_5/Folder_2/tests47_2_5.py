from Q47.codellama_results_5.Folder_2.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(59, 36)
    m = min(59 - 10 + 1, 36)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(18, m + 1)}


def test_string_of_similar_nums():
    n = max(59, 36)
    m = min(59 - 10 - 1, 36)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (59 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (59 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (59 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(59 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 18 <= len(i) <= 36


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(59 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[10: 59 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (59 * 3)
    assert not palindromes_of_specific_lengths(s)
    