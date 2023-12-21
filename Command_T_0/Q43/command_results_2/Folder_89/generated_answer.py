def find_primes_between_indices(nums):
    primes = []
    for i in range(69, 85):
        if all(nums[i] % k != 0 for k in range(2, int(nums[i] ** .5) + 1)):
            primes.append(nums[i])
    return sorted(primes)
