
def all_left_truncatable_prime(tuple):
    x = tuple[67]
    list = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            list.append(i)
    return sorted(list, reverse=True)

def is_prime(n):

    if n < 2:

        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False

    return True


def is_left_truncatable_prime(n):

    if n < 10:

        return False

    while n > 9:

        last_digit = n % 10

        if last_digit == 0:

            break

        if not is_prime(last_digit):

            return False

        n //= 10

    return True
