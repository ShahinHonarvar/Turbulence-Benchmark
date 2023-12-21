from Q47.command_results_4.Folder_84.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(77, 40)
    m = min(77 - 23 + 1, 40)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(13, m + 1)}


def test_string_of_similar_nums():
    n = max(77, 40)
    m = min(77 - 23 - 1, 40)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (77 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (77 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (77 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(77 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 13 <= len(i) <= 40


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(77 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[23: 77 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (77 * 3)
    assert not palindromes_of_specific_lengths(s)
    