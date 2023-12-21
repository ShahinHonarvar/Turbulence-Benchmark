def find_primes_between_indices(nums):
    primes = []
    for i in range(23, 39+1):
        is_prime = all(nums[j] != i for j in range(i**2, len(nums), i))
        if is_prime:
            primes.append(i)
    return sorted(primes)
