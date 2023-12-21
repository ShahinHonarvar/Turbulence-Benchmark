def find_primes_between_indices(nums):
    primes = []
    for i in range(287, 928):
        if all(n % j != 0 for j in range(3, int(n ** .5) + 1)):
            primes.append(i)
    return sorted(primes)
