from Q45.gpt_3_5_turbo_results_4.Folder_100.generated_answer import palindromes_between_indices


def test_string_of_similar_chars():
    s = ''.join('a' for _ in range(5 + 1))
    if 5 - 0 + 1 < 6:
        assert not palindromes_between_indices(s)
    else:
        assert palindromes_between_indices(s) == {'a' * i for i in range(6, 5 - 0 + 2)}


def test_string_of_distinct_chars():
    s = 'abcdefghijkl'
    assert not palindromes_between_indices(s)


def test_string_of_spaces():
    s = ' ' * (5 * 2)
    assert not palindromes_between_indices(s)


def test_string_of_same_punctuations():
    s = '@' * (5 * 2)
    assert not palindromes_between_indices(s)


def test_string_of_same_numbers():
    s = '0' * (5 * 2)
    assert not palindromes_between_indices(s)
        

def test_length_of_palindrome():
    s = ''.join('a' for _ in range(5 + 1))
    returned_result = palindromes_between_indices(s)
    for i in returned_result:
        assert 6 <= len(i) <= 5 - 0 + 1


def test_string_of_spaces_and_letters():
    s = ' a ' * (5 + 1)
    ss = s[0:5 + 1]
    ss = ss.replace(' ', '')
    length = len(ss)
    if length < 6:
        assert not palindromes_between_indices(s)
    else:
        min_ = min(length, 6)
        max_ = max(length, 6)
        assert palindromes_between_indices(s) == {'a' * i for i in range(min_, max_ + 1)}


def test_string_of_punctuations_and_letters():
    s = '%a&' * (5 + 1)
    ss = s[0:5 + 1]
    ss = ss.replace('%', '')
    ss = ss.replace('&', '')
    length = len(ss)
    if length < 6:
        assert not palindromes_between_indices(s)
    else:
        min_ = min(length, 6)
        max_ = max(length, 6)
        assert palindromes_between_indices(s) == {'a' * i for i in range(min_, max_ + 1)}
        