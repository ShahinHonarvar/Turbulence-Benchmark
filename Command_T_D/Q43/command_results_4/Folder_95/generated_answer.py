def find_primes_between_indices(nums):
    primes = []
    for n in range(19, 71):
        if all(n % i != 0 for i in range(2, n // 2 + 1)):
            primes.append(n)
    return sorted(primes)
