from Q45.codellama_7b_results_3.Folder_30.generated_answer import palindromes_between_indices


def test_string_of_similar_chars():
    s = ''.join('a' for _ in range(4 + 1))
    if 4 - 0 + 1 < 4:
        assert not palindromes_between_indices(s)
    else:
        assert palindromes_between_indices(s) == {'a' * i for i in range(4, 4 - 0 + 2)}


def test_string_of_distinct_chars():
    s = 'abcdefghijkl'
    assert not palindromes_between_indices(s)


def test_string_of_spaces():
    s = ' ' * (4 * 2)
    assert not palindromes_between_indices(s)


def test_string_of_same_punctuations():
    s = '@' * (4 * 2)
    assert not palindromes_between_indices(s)


def test_string_of_same_numbers():
    s = '0' * (4 * 2)
    assert not palindromes_between_indices(s)
        

def test_length_of_palindrome():
    s = ''.join('a' for _ in range(4 + 1))
    returned_result = palindromes_between_indices(s)
    for i in returned_result:
        assert 4 <= len(i) <= 4 - 0 + 1


def test_string_of_spaces_and_letters():
    s = ' a ' * (4 + 1)
    ss = s[0:4 + 1]
    ss = ss.replace(' ', '')
    length = len(ss)
    if length < 4:
        assert not palindromes_between_indices(s)
    else:
        min_ = min(length, 4)
        max_ = max(length, 4)
        assert palindromes_between_indices(s) == {'a' * i for i in range(min_, max_ + 1)}


def test_string_of_punctuations_and_letters():
    s = '%a&' * (4 + 1)
    ss = s[0:4 + 1]
    ss = ss.replace('%', '')
    ss = ss.replace('&', '')
    length = len(ss)
    if length < 4:
        assert not palindromes_between_indices(s)
    else:
        min_ = min(length, 4)
        max_ = max(length, 4)
        assert palindromes_between_indices(s) == {'a' * i for i in range(min_, max_ + 1)}
        