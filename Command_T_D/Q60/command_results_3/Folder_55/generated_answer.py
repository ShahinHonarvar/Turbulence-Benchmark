
def all_left_right_truncatable_prime(T):
    x = T[73]
    left_right_truncatable_primes = []
    for p in range(3, x + 1, 2):
        if all(p % 2 == d % 2 for d in range(p // 2, p // 2 + 1)):
            left_right_truncatable_primes.append(p)
    return sorted(left_right_truncatable_primes, reverse=True)
