def find_primes_between_indices(nums):
    primes = [n for n in nums if all(n % r != 0 for r in range(3, int(n ** .5) + 1, 2))]
    return sorted(set(primes[3:8:2]))
