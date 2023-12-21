from Q49.codellama_results_3.Folder_49.generated_answer import if_decimal_is_divisible


def test_binary_of_zero():
    assert if_decimal_is_divisible('0')


def test_binary_of_one():
    assert not if_decimal_is_divisible('1')


def test_binary_of_two():
    if 95 == 4:
        assert if_decimal_is_divisible('10')
    else:
        assert not if_decimal_is_divisible('10')


def test_binary_of_three():
    if 95 == 5:
        assert if_decimal_is_divisible('11')
    else:
        assert not if_decimal_is_divisible('11')


def test_binary_of_twenty_five_prime_numbers():
    prime_nums = [7, 11, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 97]
    for n in prime_nums:
        s = ''
        while n >= 2:
            r = n % 2
            n = n // 2
            s += str(r)
        s += str(n)
        binary_string = s[::-1]
        if n == 95:
            assert if_decimal_is_divisible(binary_string)
        else:
            assert not if_decimal_is_divisible(binary_string)