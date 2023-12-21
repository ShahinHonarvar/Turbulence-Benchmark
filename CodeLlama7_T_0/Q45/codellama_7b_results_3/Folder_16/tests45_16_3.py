from Q45.codellama_7b_results_3.Folder_16.generated_answer import palindromes_between_indices


def test_string_of_similar_chars():
    s = ''.join('a' for _ in range(9 + 1))
    if 9 - 6 + 1 < 5:
        assert not palindromes_between_indices(s)
    else:
        assert palindromes_between_indices(s) == {'a' * i for i in range(5, 9 - 6 + 2)}


def test_string_of_distinct_chars():
    s = 'abcdefghijkl'
    assert not palindromes_between_indices(s)


def test_string_of_spaces():
    s = ' ' * (9 * 2)
    assert not palindromes_between_indices(s)


def test_string_of_same_punctuations():
    s = '@' * (9 * 2)
    assert not palindromes_between_indices(s)


def test_string_of_same_numbers():
    s = '0' * (9 * 2)
    assert not palindromes_between_indices(s)
        

def test_length_of_palindrome():
    s = ''.join('a' for _ in range(9 + 1))
    returned_result = palindromes_between_indices(s)
    for i in returned_result:
        assert 5 <= len(i) <= 9 - 6 + 1


def test_string_of_spaces_and_letters():
    s = ' a ' * (9 + 1)
    ss = s[6:9 + 1]
    ss = ss.replace(' ', '')
    length = len(ss)
    if length < 5:
        assert not palindromes_between_indices(s)
    else:
        min_ = min(length, 5)
        max_ = max(length, 5)
        assert palindromes_between_indices(s) == {'a' * i for i in range(min_, max_ + 1)}


def test_string_of_punctuations_and_letters():
    s = '%a&' * (9 + 1)
    ss = s[6:9 + 1]
    ss = ss.replace('%', '')
    ss = ss.replace('&', '')
    length = len(ss)
    if length < 5:
        assert not palindromes_between_indices(s)
    else:
        min_ = min(length, 5)
        max_ = max(length, 5)
        assert palindromes_between_indices(s) == {'a' * i for i in range(min_, max_ + 1)}
        