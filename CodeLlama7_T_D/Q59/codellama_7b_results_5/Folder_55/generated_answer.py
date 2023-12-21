
def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[73]
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
    while n > 1 and n % 10 != 1:
        n = int(str(n)[:-1])

    if n == 1 or n % 10 == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
