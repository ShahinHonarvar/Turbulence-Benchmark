from Q47.codellama_results_1.Folder_94.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(94, 51)
    m = min(94 - 40 + 1, 51)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(45, m + 1)}


def test_string_of_similar_nums():
    n = max(94, 51)
    m = min(94 - 40 - 1, 51)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (94 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (94 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (94 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(94 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 45 <= len(i) <= 51


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(94 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[40: 94 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (94 * 3)
    assert not palindromes_of_specific_lengths(s)
    