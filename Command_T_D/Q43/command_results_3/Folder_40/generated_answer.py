def find_primes_between_indices(nums):
    return sorted(nums[1:].difference(nums[2:]), key=lambda x: x)
