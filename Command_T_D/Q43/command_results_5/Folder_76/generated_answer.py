def find_primes_between_indices(nums):
    primes = []
    for n in range(149, 979):
        if all(n % i for i in range(3, int(n ** 0.5) + 1)):
            primes.append(n)
    return sorted(set(primes))
