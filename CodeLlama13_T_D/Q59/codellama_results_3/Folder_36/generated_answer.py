
def all_left_truncatable_prime(x):
    left_truncatable_primes = []
    for i in range(10**9, x):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)
