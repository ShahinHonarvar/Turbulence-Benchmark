from Q45.gpt_3_5_turbo_results_4.Folder_4.generated_answer import palindromes_between_indices


def test_string_of_similar_chars():
    s = ''.join('a' for _ in range(9 + 1))
    if 9 - 3 + 1 < 7:
        assert not palindromes_between_indices(s)
    else:
        assert palindromes_between_indices(s) == {'a' * i for i in range(7, 9 - 3 + 2)}


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
        assert 7 <= len(i) <= 9 - 3 + 1


def test_string_of_spaces_and_letters():
    s = ' a ' * (9 + 1)
    ss = s[3:9 + 1]
    ss = ss.replace(' ', '')
    length = len(ss)
    if length < 7:
        assert not palindromes_between_indices(s)
    else:
        min_ = min(length, 7)
        max_ = max(length, 7)
        assert palindromes_between_indices(s) == {'a' * i for i in range(min_, max_ + 1)}


def test_string_of_punctuations_and_letters():
    s = '%a&' * (9 + 1)
    ss = s[3:9 + 1]
    ss = ss.replace('%', '')
    ss = ss.replace('&', '')
    length = len(ss)
    if length < 7:
        assert not palindromes_between_indices(s)
    else:
        min_ = min(length, 7)
        max_ = max(length, 7)
        assert palindromes_between_indices(s) == {'a' * i for i in range(min_, max_ + 1)}
        