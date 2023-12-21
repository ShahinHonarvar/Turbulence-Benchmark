
def all_right_truncatable_prime(tuple):
    x = tuple[52]
    right_truncatable_primes = []
    for i in range(x-1, 0, -1):
        if is_prime(i) and is_right_truncatable(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)
