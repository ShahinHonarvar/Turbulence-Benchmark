def find_primes_between_indices(nums):
    primes = []
    for i in range(17, 79 + 1):
        if all(n % i for n in nums):
            primes.append(i)
    return sorted(primes)
