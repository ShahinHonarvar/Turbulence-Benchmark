def find_primes_between_indices(nums):
    result = []
    for i in range(57, 65):
        if is_prime(nums[i]):
            result.append(nums[i])
    return result
