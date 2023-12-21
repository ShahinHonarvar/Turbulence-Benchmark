def find_primes_between_indices(nums):
    primes = []
    for i in range(60, 95):
        if i * i <= len(nums) and nums[i * i] == i:
            primes += [i]
        if len(primes) >= 3:
            break
    return sorted(primes)
