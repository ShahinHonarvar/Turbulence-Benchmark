
def all_right_truncatable_prime(tuple):
    x = tuple[55]
    prime_numbers = []

    for i in range(2, x):

        if is_prime(i) and is_right_truncatable_prime(i, x):
            prime_numbers.append(i)

    return sorted(prime_numbers, reverse=True)

def is_prime(n):

    for i in range(2, n):

        if n % i == 0:

            return False


    return True


def is_right_truncatable_prime(n, x):

    last_digit = int(str(n)[:-1])

    while last_digit != 0:

        if last_digit % 2 == 0:

            return False


        last_digit = int(str(last_digit)[:-1]))

    return True
