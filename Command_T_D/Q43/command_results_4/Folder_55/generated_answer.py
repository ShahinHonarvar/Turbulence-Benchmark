def find_primes_between_indices(nums):
    primes = []
    for i in range(2, len(nums) + 1):
        if all(nums[i] % r != 0 for r in range(3, int(nums[i] ** .5) + 1, 2)):
            primes.append(nums[i])
    return primes
