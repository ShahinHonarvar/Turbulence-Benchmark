def find_primes_between_indices(nums):
    primes = []
    for i in range(28, 83):
        if not any(nums[i] % x == 0 for x in range(2, int(nums[i] ** .5) + 1)):
            primes.append(nums[i])
    return primes
