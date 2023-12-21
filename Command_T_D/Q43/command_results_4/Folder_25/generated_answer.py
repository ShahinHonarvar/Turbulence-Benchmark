def find_primes_between_indices(nums):
    start, stop = nums.index(52), nums.index(53)
    return sorted(nums[start:stop+1])
