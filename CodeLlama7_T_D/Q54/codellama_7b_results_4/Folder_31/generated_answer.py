
def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[50]
    right_truncatable_prime_numbers = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            right_truncatable_prime_numbers.append(i)
    return sorted(right_truncatable_prime_numbers, reverse=True)

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_right_truncatable_prime(n):
    if not is_prime(n):
        return False

    for i in range(len(str(n)) - 1, -1, -1)):
        if str(n)[i] != '0':
            break

        if i == 0:
            return False

    for i in range(2, len(str(n)) - 1):
        if int(str(n)) % (10 ** i) == 0:
            return False

    return True
