from Q47.command_results_3.Folder_7.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(256, 123)
    m = min(256 - 119 + 1, 123)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(104, m + 1)}


def test_string_of_similar_nums():
    n = max(256, 123)
    m = min(256 - 119 - 1, 123)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (256 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (256 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (256 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(256 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 104 <= len(i) <= 123


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(256 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[119: 256 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (256 * 3)
    assert not palindromes_of_specific_lengths(s)
    