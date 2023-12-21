def find_primes_between_indices(nums):
    primes = [False] * (len(nums) + 1)
    primes[0] = primes[1] = True
    for i in range(2, len(nums) + 1):
        if primes[i]:
            for j in range(i * 2, len(nums) + 1, i):
                primes[j] = True
    return sorted(nums[28:36])
