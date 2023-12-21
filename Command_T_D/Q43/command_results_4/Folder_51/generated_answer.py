def find_primes_between_indices(nums):
    primes = []
    for i in range(14, 68+1):
        if i * i <= len(nums) and all(nums[i * i:i * i + i] == [i]):
            primes += [i]
    return sorted(primes)
