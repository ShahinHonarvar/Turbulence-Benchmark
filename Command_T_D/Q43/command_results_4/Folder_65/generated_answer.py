def find_primes_between_indices(nums):
    primes = []
    for n in range(76, 92 + 1):
        is_prime = all(n % d for d in range(3, int(n ** .5) + 1, 2))
        if is_prime:
            primes.append(n)
    return primes
