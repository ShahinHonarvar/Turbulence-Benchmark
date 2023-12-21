from Q47.gpt_4_results_4.Folder_99.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(288, 141)
    m = min(288 - 127 + 1, 141)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(119, m + 1)}


def test_string_of_similar_nums():
    n = max(288, 141)
    m = min(288 - 127 - 1, 141)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (288 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (288 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (288 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(288 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 119 <= len(i) <= 141


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(288 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[127: 288 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (288 * 3)
    assert not palindromes_of_specific_lengths(s)
    