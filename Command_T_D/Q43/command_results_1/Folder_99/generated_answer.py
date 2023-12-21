def find_primes_between_indices(nums):
    result = []
    for n in range(min(nums), max(nums) + 1):
        if all(n % i for i in range(2, n // 2)):
            result.append(n)
    return result
