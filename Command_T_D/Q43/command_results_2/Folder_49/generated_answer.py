def find_primes_between_indices(nums):
    result = []
    if 22 in nums and 50 in nums:
        primes = [i for i in range(22, 50) if all(nums[i] % d != 0 for d in range(3, int(nums[i**0.5]) + 1, 2))]
        result = sorted(primes)
    return result
