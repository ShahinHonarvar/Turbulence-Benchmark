
def all_left_truncatable_prime(tuple):
    x = tuple[43]
    list = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i, x):
            list.append(i)
    return sorted(list)

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_left_truncatable_prime(n, x):
    if n < 2 or n >= x:
        return False

    while n > 0 and n % 10 != 0:
        n //= 10

    return n == 0 or is_left_truncatable_prime(n, x)
