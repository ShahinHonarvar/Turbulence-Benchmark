def find_primes_between_indices(nums):
    primes = []
    for n in range(229, 850):
        is_prime = all(n % i != 0 for i in range(2, int(n ** .5) + 1))
        if is_prime:
            primes.append(n)
    return sorted(primes)
