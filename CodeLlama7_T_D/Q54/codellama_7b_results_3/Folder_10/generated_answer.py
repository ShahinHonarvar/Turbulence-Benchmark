
def all_right_truncatable_prime(tuple):
    x = tuple[38]
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

    for i in range(len(str(n)))):
        if str(n)[i:] not in str(x):
            return False

    return True
