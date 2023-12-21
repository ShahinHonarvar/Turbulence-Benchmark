
def all_left_right_truncatable_prime(tuple):
    x = tuple[86]
    prime_numbers = []
    for i in range(2, x + 1):
        if is_prime(i) and is_left_right_truncatable_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers)

def is_prime(n):

    if n < 2:

        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False

    return True

def is_left_right_truncatable_prime(n):

    if len(str(n)) > 2:

        return False

    digits = list(map(int, str(n)))

    for i in range(1, len(digits)):

        if digits[i] == 0:

            return False

        if n % (10 ** i) != digits[i]:

            return False

    return True
