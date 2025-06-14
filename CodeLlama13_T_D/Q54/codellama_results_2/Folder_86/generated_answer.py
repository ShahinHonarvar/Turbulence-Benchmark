
def all_right_truncatable_prime(x):
    right_truncatable_primes = []
    for i in range(10**126):
        if is_prime(i) and is_right_truncatable_prime(i, x):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)
