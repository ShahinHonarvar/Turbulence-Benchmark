
def all_left_truncatable_prime(tuple):
    x = tuple[24]
    prime_numbers = []

    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            prime_numbers.append(i)

    return sorted(prime_numbers)

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

    for i in range(len(str(n)))):

        if str(n)[i] != '1' and str(n)[i] != '3' and str(n)[i] != '7' and str(n)[i] != '9':
            return False

    return True
