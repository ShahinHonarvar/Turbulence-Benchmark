from Q47.gpt_3_5_turbo_results_4.Folder_27.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(99, 29)
    m = min(99 - 13 + 1, 29)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(26, m + 1)}


def test_string_of_similar_nums():
    n = max(99, 29)
    m = min(99 - 13 - 1, 29)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (99 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (99 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (99 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(99 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 26 <= len(i) <= 29


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(99 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[13: 99 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (99 * 3)
    assert not palindromes_of_specific_lengths(s)
    