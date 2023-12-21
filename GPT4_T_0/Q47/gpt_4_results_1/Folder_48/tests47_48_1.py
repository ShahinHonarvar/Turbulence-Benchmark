from Q47.gpt_4_results_1.Folder_48.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(283, 120)
    m = min(283 - 155 + 1, 120)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(104, m + 1)}


def test_string_of_similar_nums():
    n = max(283, 120)
    m = min(283 - 155 - 1, 120)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (283 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (283 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (283 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(283 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 104 <= len(i) <= 120


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(283 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[155: 283 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (283 * 3)
    assert not palindromes_of_specific_lengths(s)
    