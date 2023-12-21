from Q47.gpt_4_results_2.Folder_93.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(95, 49)
    m = min(95 - 17 + 1, 49)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(13, m + 1)}


def test_string_of_similar_nums():
    n = max(95, 49)
    m = min(95 - 17 - 1, 49)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (95 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (95 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (95 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(95 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 13 <= len(i) <= 49


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(95 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[17: 95 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (95 * 3)
    assert not palindromes_of_specific_lengths(s)
    