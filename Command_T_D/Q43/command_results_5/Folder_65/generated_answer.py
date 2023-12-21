def find_primes_between_indices(nums):
    primes = []
    for i in range(76, 92):
        if all(nums[i] % j for j in range(2, int(nums[i] ** .5) + 1)):
            primes.append(nums[i])
    return sorted(primes)
