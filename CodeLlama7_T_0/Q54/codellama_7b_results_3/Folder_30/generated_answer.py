
def all_right_truncatable_prime(tuple):
    x = tuple[37]
    prime_numbers = []

    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            prime_numbers.append(i)

    return sorted(prime_numbers, reverse=True)

def is_prime(n):

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_right_truncatable_prime(n):

    while n > 0:

        if n % 10 == 0:

            n = int(n / 10)

        else:

            break


    return is_prime(n)
