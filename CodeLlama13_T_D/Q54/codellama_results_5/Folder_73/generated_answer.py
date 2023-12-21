
def all_right_truncatable_prime(tuple):
    x = tuple[97]
    right_truncatable_primes = []
    for i in range(2, x+1):
        if is_prime(i) and all(is_prime(i%(10**j)) for j in range(1, int(log10(x)))):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)
