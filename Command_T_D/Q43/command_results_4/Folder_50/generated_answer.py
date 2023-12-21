def find_primes_between_indices(nums):
    primes = []
    for i in range(23, 59 + 1):
        if all(nums[j] != i for j in range(23, 59 + 1)):
            primes.append(i)
    return sorted(set(primes))
