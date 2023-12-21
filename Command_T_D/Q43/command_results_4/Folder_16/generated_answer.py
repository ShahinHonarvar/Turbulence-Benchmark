def find_primes_between_indices(nums):
    primes = []
    for i in range(424, 552 + 1):
        is_prime = all(nums[j] != i for j in range(424, 552 + 1))
        if is_prime:
            primes.append(i)
    return sorted(primes)
