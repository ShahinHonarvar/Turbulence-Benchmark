
def all_right_truncatable_prime(tuple):
    x = tuple[618]
    prime_numbers = []

    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            prime_numbers.append(i)

    return sorted(prime_numbers)

def is_prime(n):

    if n < 2:

        return False


    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False


    return True


def is_right_truncatable_prime(n):

    digits = [int(digit) for digit in str(n)]

    for i in range(len(digits)):

        if not is_prime(int("".join(map(str, digits[i:])))))):

            return False


    return True
