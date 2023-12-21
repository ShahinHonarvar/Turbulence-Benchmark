def find_primes_between_indices(nums):
    primes = []
    for i in range(430, 805):
        if all(n % j != 0 for j in range(2, int(n**(0.5)) + 1)):
            primes.append(i)
    return sorted(primes)
