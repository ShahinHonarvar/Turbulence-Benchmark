from Q47.command_results_3.Folder_66.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(79, 41)
    m = min(79 - 32 + 1, 41)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(35, m + 1)}


def test_string_of_similar_nums():
    n = max(79, 41)
    m = min(79 - 32 - 1, 41)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (79 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (79 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (79 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(79 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 35 <= len(i) <= 41


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(79 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[32: 79 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (79 * 3)
    assert not palindromes_of_specific_lengths(s)
    