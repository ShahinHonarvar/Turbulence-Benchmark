def find_primes_between_indices(nums):
    primes = [True] * (len(nums) + 1)
    primes[0] = primes[1] = False
    for i in range(2, len(nums)):
        if primes[i]:
            for j in range(i + i, len(nums), i):
                primes[j] = False
    return sorted(nums[27:86]) if primes[27] and primes[86] else []
