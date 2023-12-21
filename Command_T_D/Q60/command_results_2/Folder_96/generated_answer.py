
def all_left_right_truncatable_prime(x):
    return sorted(list(filter(left_right_truncatable_prime, range(2, x+1))), key=lambda x: x)

def left_right_truncatable_prime(x):
    return is_prime(x) and left_right_truncatable_digit_prime(x)

def left_right_truncatable_digit_prime(x):
    return is_digit_prime(x) and left_right_truncatable_two_digit_prime(x)

def left_right_truncatable_two_digit_prime(x):
    return is_two_digit_prime(x) and left_right_truncatable_three_digit_prime(x)

def left_right_truncatable_three_digit_prime(x):
    return is_three_digit_prime(x) and left_right_truncatable_four_digit_prime(x)

def left_right_truncatable_four_digit_prime(x):
    return is_four_digit_prime(x)

def is_prime(x):
    return x > 1 and all(x % d for d in range(3, int(x ** .5) + 1, 2))

def is_digit_prime(x):
    return all(x % 10 != d for d in range(10))

def is_two_digit_prime(x):
    return x in (11, 31, 37, 71, 93, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941)

def is_three_digit_prime(x):
    return x in (31, 37, 41, 43, 59, 61, 89, 107, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941)

def is_four_digit_prime(x):
    return x in (2121, 2131, 2179, 2203, 2281, 3217, 4253, 4423, 9689, 9941)
