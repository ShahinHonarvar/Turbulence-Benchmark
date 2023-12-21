
def all_right_truncatable_prime(n):
    prime_numbers = []

    for i in range(2, n+1):
        if is_prime(i) and is_right_truncatable_prime(i):
            prime_numbers.append(i)

    return sorted(prime_numbers, reverse=True)

def is_prime(n):

    for i in range(2, n+1):
        if n % i == 0:
            return False

    return True


def is_right_truncatable_prime(n):

    while n > 0:

        if n % 10 == 0:
            return False

        n = n // 10

    return True
