
def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[14]
    right_truncatable_primes = []
    for i in range(x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)

def is_right_truncatable_prime(n):
    if n < 2:
        return False
    for i in range(1, int(len(str(n)) / 2)):
        if not is_prime(n - (10**i)):
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
