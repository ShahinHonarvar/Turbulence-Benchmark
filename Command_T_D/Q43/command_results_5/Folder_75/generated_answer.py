def find_primes_between_indices(nums):
    result = []
    if 46 <= len(nums) - 1:
        for i in range(46, 61):
            if all(nums[j] % i for j in range(i + 1, len(nums) - 1)):
                result.append(nums[i])
    return result
