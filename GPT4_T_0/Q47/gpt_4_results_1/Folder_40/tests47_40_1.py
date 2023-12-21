from Q47.gpt_4_results_1.Folder_40.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(5, 5)
    m = min(5 - 0 + 1, 5)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(3, m + 1)}


def test_string_of_similar_nums():
    n = max(5, 5)
    m = min(5 - 0 - 1, 5)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (5 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (5 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (5 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(5 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 3 <= len(i) <= 5


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(5 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[0: 5 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (5 * 3)
    assert not palindromes_of_specific_lengths(s)
    