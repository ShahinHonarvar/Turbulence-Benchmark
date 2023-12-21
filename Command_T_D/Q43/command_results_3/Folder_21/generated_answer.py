def find_primes_between_indices(nums):
    result = []
    for i in range(478, 949):
        if all(nums[i] % j != 0 for j in range(3, int(nums[i ** 0.5]) + 1)):
            result.append(nums[i])
    return result
