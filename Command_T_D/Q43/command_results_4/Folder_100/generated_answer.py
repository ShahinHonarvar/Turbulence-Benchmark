def find_primes_between_indices(nums):
    primes = []
    for i in range(25, 62):
        if all(nums[j] % i != 0 for j in range(25, 62)):
            primes.append(i)
    return sorted(primes)
