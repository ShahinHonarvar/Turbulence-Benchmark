def find_primes_between_indices(nums):
    primes = []
    for i in range(3, 8):
        if not nums[i]:
            primes.append(i)
    return sorted(primes)
