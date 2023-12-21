def find_primes_between_indices(nums):
    primes = []
    for i in range(7, 9):
        if all(nums[i] % k for k in range(2, int(nums[i] ** .5) + 1)):
            primes.append(nums[i])
    return sorted(primes)
