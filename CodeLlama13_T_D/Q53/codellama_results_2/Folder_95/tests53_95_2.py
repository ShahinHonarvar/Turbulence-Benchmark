from Q53.codellama_results_2.Folder_95.generated_answer import palindrome_of_length_at_least_n
import string
import random


def test_string_of_similar_chars_of_length_35():
    s = ''.join('a' for _ in range(35))
    assert palindrome_of_length_at_least_n(s) == {s}


def test_string_of_similar_chars_of_length_greater_than_35():
    ss = ''.join('a' for _ in range(35 * 2))
    s = ss[:35]
    result = []
    for i in range(0, 35 + 1):
        result.append(s + ('a' * i))
    assert palindrome_of_length_at_least_n(ss) == set(result)


def test_string_of_many_chars():
    s = 'abcdef'
    r = ''
    for _ in range(35):
        r += s
    assert not palindrome_of_length_at_least_n(r)


def test_string_of_spaces():
    s = ' ' * (35 * 2)
    assert not palindrome_of_length_at_least_n(s)


def test_string_of_spaces_and_letters():
    s = ' a ' * 35 * 2
    ss = s.replace(' ','')
    sss = ss[:35]
    result = []
    for i in range(0, 35 + 1):
        result.append(sss + ('a' * i))
    assert not palindrome_of_length_at_least_n(s)


def test_string_of_punctuations():
    s = ''.join(random.choice(string.punctuation) for _ in range(35))
    assert not palindrome_of_length_at_least_n(s)


def test_string_of_punctuations_and_letters():
    s = 'a%' * 35
    assert not palindrome_of_length_at_least_n(s)


def test_string_of_many_punctuations_and_letters():
    s = 'a%' * 35 * 2
    assert not palindrome_of_length_at_least_n(s)


def test_string_of_many_punctuations_and_letters_and_spaces():
    s = 'a% ' * 35 * 2
    assert not palindrome_of_length_at_least_n(s)


def test_length_of_palindrome():
    n = random.randint(5,10)
    s = 'a' * (35 * n)
    returned_result = palindrome_of_length_at_least_n(s)
    for i in returned_result:
        assert 35 <= len(i)


def test_string_of_similar_nums():
    s = ''.join('0' for _ in range(35))
    assert not palindrome_of_length_at_least_n(s)


def test_string_of_many_similar_nums():
    ss = ''.join('0' for _ in range(35 * 2))
    s = ss[:35]
    result = []
    for i in range(0, 35 + 1):
        result.append(s + ('0' * i))
    assert not palindrome_of_length_at_least_n(ss)


def test_numeric_string():
    s = ''.join(random.choice(string.digits) for _ in range(35 // 2))
    if 35 % 2 == 0:
        s += s[::-1]
    else:
        s += (random.choice(string.digits) + s[::-1])
    assert not palindrome_of_length_at_least_n(s)
    