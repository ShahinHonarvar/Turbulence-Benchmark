def find_primes_between_indices(nums):
    return sorted([x for x in nums[28:36] if all(x % i for i in range(2, x // 2))])
