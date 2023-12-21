from Q47.gpt_4_results_5.Folder_86.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(95, 55)
    m = min(95 - 30 + 1, 55)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(34, m + 1)}


def test_string_of_similar_nums():
    n = max(95, 55)
    m = min(95 - 30 - 1, 55)
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
        assert 34 <= len(i) <= 55


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(95 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[30: 95 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (95 * 3)
    assert not palindromes_of_specific_lengths(s)
    