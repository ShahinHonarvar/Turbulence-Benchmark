def find_primes_between_indices(nums):
    result = []
    for i in range(28, 37):
        if all(nums[i] % j != 0 for j in range(2, int(nums[i**0.5]) + 1)):
            result.append(nums[i])
    return result
