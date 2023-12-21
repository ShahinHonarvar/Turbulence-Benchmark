def find_primes_between_indices(nums):
    primes = []
    for i in range(31, 67):
        if all(num % d != 0 for d in range(2, i//2 + 1)):
            primes.append(i)
    return sorted(primes)
