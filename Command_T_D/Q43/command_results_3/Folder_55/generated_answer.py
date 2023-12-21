def find_primes_between_indices(nums):
    result = []
    for i in range(2, len(nums) + 1):
        if nums[i] > 2:
            result += [nums[i]]
    return sorted(result)
