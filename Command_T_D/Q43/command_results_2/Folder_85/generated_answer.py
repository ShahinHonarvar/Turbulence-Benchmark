def find_primes_between_indices(nums):
    primes = []
    for n in range(32, 35):
        if n in nums:
            continue
        if all(n % i != 0 for i in range(2, int(n ** .5) + 1)):
            primes.append(n)
    return sorted(primes)
