
def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[8]
    list_of_all_left_truncatable_prime_numbers_less_than_x = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            list_of_all_left_truncatable_prime_numbers_less_than_x.append(i)
    return sorted(list_of_all_left_truncatable_prime_numbers_less_than_x, reverse=True)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_truncatable_prime(n):
    if str(n)[0] == '0':
        return False

    for i in range(1, len(str(n)))):
        if int(str(n)[:i]) != n % 10 ** i:
            return False

    return True
