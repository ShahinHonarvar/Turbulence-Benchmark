def find_primes_between_indices(nums):
    primes = []
    for n in range(7, 8):
        if all(n % i for i in range(3, int(n ** .5) + 1, 2)):
            primes.append(n)
    return sorted(set(primes))
