
def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[14]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)

def is_right_truncatable_prime(n):
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
