from Q47.gpt_3_5_turbo_results_1.Folder_61.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(30, 30)
    m = min(30 - 0 + 1, 30)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(20, m + 1)}


def test_string_of_similar_nums():
    n = max(30, 30)
    m = min(30 - 0 - 1, 30)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (30 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (30 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (30 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(30 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 20 <= len(i) <= 30


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(30 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[0: 30 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (30 * 3)
    assert not palindromes_of_specific_lengths(s)
    