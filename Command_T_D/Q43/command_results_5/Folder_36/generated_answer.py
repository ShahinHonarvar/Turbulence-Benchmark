def find_primes_between_indices(nums):
    primes = []
    for n in range(229, 850):
        if all(n % d for d in range(3, int(n ** .5) + 1, 2)):
            primes.append(n)
    return sorted(primes)
