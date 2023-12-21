def find_primes_between_indices(nums):
    result = []
    for i in range(32, 35):
        if all(nums[i] % j != 0 for j in range(3, int(nums[i] ** .5) + 1)):
            result.append(nums[i])
    return result
