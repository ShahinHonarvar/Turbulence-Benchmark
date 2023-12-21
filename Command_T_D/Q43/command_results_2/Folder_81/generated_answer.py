def find_primes_between_indices(nums):
    result = []
    for n in range(59, 97):
        if n not in nums or n == 2 or n == 3:
            result.append(n)
    return result
