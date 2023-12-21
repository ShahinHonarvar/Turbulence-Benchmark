from Q47.codellama_results_2.Folder_68.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(50, 100)
    m = min(50 - 0 + 1, 100)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(50, m + 1)}


def test_string_of_similar_nums():
    n = max(50, 100)
    m = min(50 - 0 - 1, 100)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (50 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (50 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (50 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(50 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 50 <= len(i) <= 100


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(50 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[0: 50 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (50 * 3)
    assert not palindromes_of_specific_lengths(s)
    