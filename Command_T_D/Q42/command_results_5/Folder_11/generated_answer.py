def prime_factors(nums):
    return set(int(d) for d in range(2, int(nums[77]) + 1) if all(nums[i] % d == 0 for i in range(77) if nums[i] != 0))
