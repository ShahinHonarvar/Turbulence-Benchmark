def find_primes_between_indices(nums):
    primes = []
    for i in range(112, 361):
        if all(nums[i] % r != 0 for r in range(2, int(nums[i] ** .5) + 1)):
            primes.append(nums[i])
    return sorted(primes)
