from Q47.codellama_7b_results_3.Folder_11.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(97, 36)
    m = min(97 - 24 + 1, 36)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(10, m + 1)}


def test_string_of_similar_nums():
    n = max(97, 36)
    m = min(97 - 24 - 1, 36)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (97 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (97 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (97 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(97 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 10 <= len(i) <= 36


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(97 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[24: 97 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (97 * 3)
    assert not palindromes_of_specific_lengths(s)
    