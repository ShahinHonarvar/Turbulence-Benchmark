
def all_left_truncatable_prime(x):
    primes = []
    for i in range(2, x):
        if is_prime(i) and '0' not in str(i):
            primes.append(i)
    return primes

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
