def find_primes_between_indices(nums):
    result = []
    for i in range(75, 85):
        if all(nums[j] % i != 0 for j in range(i + 1, len(nums) + 1)):
            result.append(nums[i])
    return result
