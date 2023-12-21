def find_primes_between_indices(nums):
    lst = range(43, 60)
    if len(nums) == 0:
        return []
    primes = [x for x in nums if all(nums[i] % x for i in range(1, len(nums) + 1)) == 0]
    return sorted(set(primes), reverse=True)
