def find_primes_between_indices(nums):
    result = []
    for i in range(43, 59 + 1):
        if all(n % i for n in nums):
            result.append(i)
    return result
