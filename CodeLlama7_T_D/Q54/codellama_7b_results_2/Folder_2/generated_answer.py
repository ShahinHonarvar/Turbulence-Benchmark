
def all_right_truncatable_prime(tuple):
    x = tuple[618]
    list = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            list.append(i)
    return sorted(list)

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_right_truncatable_prime(n):
    if n < 10:
        return False

    while n > 0:
        last_digit = n % 10
        if last_digit == 0 or last_digit == 5 or last_digit == 6:
            return False

        n //= 10

    return True
