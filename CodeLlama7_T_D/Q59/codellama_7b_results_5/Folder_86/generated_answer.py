
def all_left_truncatable_prime(tuple):
    x = tuple[126]
    prime_numbers = []

    for i in range(10, x):
        if is_prime(i) and left_truncatable_prime(i):
            prime_numbers.append(i)

    return sorted(prime_numbers, reverse=True)

def is_prime(n):

    if n < 2:

        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False

    return True


def left_truncatable_prime(n):

    if str(n)[0] == '0':

        return False

    for i in range(1, len(str(n)))):

        if int(str(n)[0:i]) != 0 and not is_prime(int(str(n)[0:i]))):

            return False

    return True
