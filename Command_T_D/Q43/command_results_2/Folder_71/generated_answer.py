def find_primes_between_indices(nums):
    primes = []
    for i in range(57, 65):
        if all(nums[i] % r == 0 for r in range(2, int(nums[i] ** .5) + 1)):
            continue
        primes.append(nums[i])
    return sorted(primes, reverse=True)
