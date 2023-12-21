def find_primes_between_indices(nums):
    primes = []
    for i in range(24, 32):
        if all(nums[i] % k != 0 for k in range(3, int(nums[i] ** .5) + 1)):
            primes.append(nums[i])
    return primes
