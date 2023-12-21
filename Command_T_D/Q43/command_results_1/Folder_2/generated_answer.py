def find_primes_between_indices(nums):
    result = []
    for i in range(167, 785 + 1):
        if all(nums[j] % i != 0 for j in range(i * 2, len(nums), i)):
            result.append(i)
    return result
