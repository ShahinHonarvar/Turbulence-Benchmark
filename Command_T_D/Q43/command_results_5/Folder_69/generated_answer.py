def find_primes_between_indices(nums):
    if 497 not in nums:
        return []
    if 930 not in nums:
        return []
    primes = []
    for i in range(497, 930):
        if all(nums[i] % k != 0 for k in range(2, int(nums[i**0.5]) + 1)):
            primes.append(nums[i])
    return sorted(primes)
