from Q53.codellama_results_5.Folder_40.generated_answer import palindrome_of_length_at_least_n
import string
import random


def test_string_of_similar_chars_of_length_3():
    s = ''.join('a' for _ in range(3))
    assert palindrome_of_length_at_least_n(s) == {s}


def test_string_of_similar_chars_of_length_greater_than_3():
    ss = ''.join('a' for _ in range(3 * 2))
    s = ss[:3]
    result = []
    for i in range(0, 3 + 1):
        result.append(s + ('a' * i))
    assert palindrome_of_length_at_least_n(ss) == set(result)


def test_string_of_many_chars():
    s = 'abcdef'
    r = ''
    for _ in range(3):
        r += s
    assert not palindrome_of_length_at_least_n(r)


def test_string_of_spaces():
    s = ' ' * (3 * 2)
    assert not palindrome_of_length_at_least_n(s)


def test_string_of_spaces_and_letters():
    s = ' a ' * 3 * 2
    ss = s.replace(' ','')
    sss = ss[:3]
    result = []
    for i in range(0, 3 + 1):
        result.append(sss + ('a' * i))
    assert not palindrome_of_length_at_least_n(s)


def test_string_of_punctuations():
    s = ''.join(random.choice(string.punctuation) for _ in range(3))
    assert not palindrome_of_length_at_least_n(s)


def test_string_of_punctuations_and_letters():
    s = 'a%' * 3
    assert not palindrome_of_length_at_least_n(s)


def test_string_of_many_punctuations_and_letters():
    s = 'a%' * 3 * 2
    assert not palindrome_of_length_at_least_n(s)


def test_string_of_many_punctuations_and_letters_and_spaces():
    s = 'a% ' * 3 * 2
    assert not palindrome_of_length_at_least_n(s)


def test_length_of_palindrome():
    n = random.randint(5,10)
    s = 'a' * (3 * n)
    returned_result = palindrome_of_length_at_least_n(s)
    for i in returned_result:
        assert 3 <= len(i)


def test_string_of_similar_nums():
    s = ''.join('0' for _ in range(3))
    assert not palindrome_of_length_at_least_n(s)


def test_string_of_many_similar_nums():
    ss = ''.join('0' for _ in range(3 * 2))
    s = ss[:3]
    result = []
    for i in range(0, 3 + 1):
        result.append(s + ('0' * i))
    assert not palindrome_of_length_at_least_n(ss)


def test_numeric_string():
    s = ''.join(random.choice(string.digits) for _ in range(3 // 2))
    if 3 % 2 == 0:
        s += s[::-1]
    else:
        s += (random.choice(string.digits) + s[::-1])
    assert not palindrome_of_length_at_least_n(s)
    