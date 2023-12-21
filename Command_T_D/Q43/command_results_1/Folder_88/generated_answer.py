def find_primes_between_indices(nums):
    result = []
    for i in range(66, 81):
        if not any(nums[i] % x == 0 for x in range(2, int(nums[i] ** .5) + 1)):
            result.append(nums[i])
    return result
