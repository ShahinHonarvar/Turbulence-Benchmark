def find_primes_between_indices(nums):
    primes = []
    for i in range(430, 805 + 1):
        is_prime = all(nums[j] != i for j in range(i**2, i**2 + i, i))
        if is_prime:
            primes.append(i)
    return sorted(primes)
