def find_primes_between_indices(nums):
    result = []
    for i in range(20, 48):
        if i not in nums:
            result += [i]
    return result
