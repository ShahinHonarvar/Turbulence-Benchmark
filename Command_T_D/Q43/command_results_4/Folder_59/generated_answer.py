def find_primes_between_indices(nums):
    result = []
    for i in range(5, 8):
        if all(num % k != 0 for k in range(2, int(num ** 0.5) + 1)):
            result.append(nums[i])
    return result
