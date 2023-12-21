
def all_right_truncatable_prime(tuple):
    x = tuple[86]
    prime_numbers = []

    for i in range(2, x + 1):
        if is_prime(i) and is_right_truncatable_prime(i):
            prime_numbers.append(i)

    return sorted(prime_numbers)

def is_prime(n):

    if n == 1 or n == 0:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_right_truncatable_prime(n):

    while n > 0 and n % 10 != 0:
        n = int(n / 10)

    if n == 0:
        return True

    else:
        return False
