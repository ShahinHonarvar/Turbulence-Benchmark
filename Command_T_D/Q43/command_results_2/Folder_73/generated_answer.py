def find_primes_between_indices(nums):
    primes = []
    for i in range(19, 90):
        if all(nums[i] % r for r in range(3, int(nums[i] ** .5) + 1, 2)):
            primes.append(nums[i])
    return sorted(primes)
