
def all_right_truncatable_prime(tuple):
    x = tuple[466]
    prime_numbers = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i, x):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_right_truncatable_prime(n, x):
    if n < 2 or x <= n:
        return False

    for i in range(1, int(x ** 0.5) + 1):
        if n % i == 0 and is_prime(int(n / i)) and (n / i) < x:
            return True

    return False
