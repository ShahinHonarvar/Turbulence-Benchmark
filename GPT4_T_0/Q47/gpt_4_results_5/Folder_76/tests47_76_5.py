from Q47.gpt_4_results_5.Folder_76.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(292, 182)
    m = min(292 - 101 + 1, 182)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(154, m + 1)}


def test_string_of_similar_nums():
    n = max(292, 182)
    m = min(292 - 101 - 1, 182)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (292 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (292 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (292 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(292 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 154 <= len(i) <= 182


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(292 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[101: 292 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (292 * 3)
    assert not palindromes_of_specific_lengths(s)
    