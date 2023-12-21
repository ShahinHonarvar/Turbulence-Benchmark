from Q47.gpt_4_results_5.Folder_62.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(87, 56)
    m = min(87 - 26 + 1, 56)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(52, m + 1)}


def test_string_of_similar_nums():
    n = max(87, 56)
    m = min(87 - 26 - 1, 56)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (87 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (87 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (87 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(87 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 52 <= len(i) <= 56


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(87 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[26: 87 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (87 * 3)
    assert not palindromes_of_specific_lengths(s)
    