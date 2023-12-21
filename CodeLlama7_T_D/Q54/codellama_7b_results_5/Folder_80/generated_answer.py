
def all_right_truncatable_prime(tuple):
    x = tuple[14]
    prime_numbers = []

    for i in range(2, x + 1):
        if is_prime(i) and is_right_truncatable_prime(i):
            prime_numbers.append(i)

    return sorted(prime_numbers, reverse=True)

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


    for i in range(1, len(str(n)))):

        if n % 10 ** i == 0:

            return False


    return True
