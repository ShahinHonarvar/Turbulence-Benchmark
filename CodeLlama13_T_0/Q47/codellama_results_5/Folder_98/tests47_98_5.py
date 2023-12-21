from Q47.codellama_results_5.Folder_98.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(20, 80)
    m = min(20 - 0 + 1, 80)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(5, m + 1)}


def test_string_of_similar_nums():
    n = max(20, 80)
    m = min(20 - 0 - 1, 80)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (20 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (20 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (20 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(20 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 5 <= len(i) <= 80


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(20 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[0: 20 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (20 * 3)
    assert not palindromes_of_specific_lengths(s)
    