
def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[96]
    list_of_all_right_truncatable_prime_numbers_less_than_x = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            list_of_all_right_truncatable_prime_numbers_less_than_x.append(i)
    return sorted(list_of_all_right_truncatable_prime_numbers_less_than_x, reverse=True)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_right_truncatable_prime(n):
    str_n = str(n)
    for i in range(len(str_n) - 1, -1, -1):
        if int(str_n[:i]) != n % 10 ** (len(str_n) - i)):
            return False

    return True
