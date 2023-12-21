
def all_left_right_truncatable_prime(x):
    prime_numbers = []
    for i in range(1, x + 1):
        if is_prime(i) and is_left_right_truncatable_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_left_right_truncatable_prime(n):
    if str(n)[0] != '1' and str(n)[-1:] != '1':
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if pow(i, n - 1, n) != 1:
            return False

    return True
