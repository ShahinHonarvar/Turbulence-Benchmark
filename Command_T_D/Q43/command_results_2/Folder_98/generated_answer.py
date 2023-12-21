def find_primes_between_indices(nums):
    result = []
    for i in range(1, len(nums)):
        if all(nums[i] % k for k in range(3, int(nums[i] ** 0.5) + 1, 2)):
            result.append(nums[i])
    return result
