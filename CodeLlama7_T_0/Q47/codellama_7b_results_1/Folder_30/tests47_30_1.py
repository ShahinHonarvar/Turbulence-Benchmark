from Q47.codellama_7b_results_1.Folder_30.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(90, 71)
    m = min(90 - 14 + 1, 71)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(55, m + 1)}


def test_string_of_similar_nums():
    n = max(90, 71)
    m = min(90 - 14 - 1, 71)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (90 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (90 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (90 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(90 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 55 <= len(i) <= 71


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(90 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[14: 90 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (90 * 3)
    assert not palindromes_of_specific_lengths(s)
    