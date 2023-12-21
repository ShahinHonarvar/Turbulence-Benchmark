
def all_right_truncatable_prime(tuple):
    x = tuple[630]
    prime_numbers = []

    for i in range(2, x):
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

    string_n = str(n)

    for i in range(len(string_n)):

        if not is_prime(int(string_n[:i] + string_n[i+1:])):

            return False


    return True
