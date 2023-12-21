def find_primes_between_indices(nums):
    primes = [True] * (len(nums) + 1)
    primes[0] = primes[1] = False
    for i in range(2, len(nums) + 1):
        if primes[i]:
            for j in range(i + i, len(nums) + 1, i):
                primes[j] = False
    return sorted(nums[229:850])
