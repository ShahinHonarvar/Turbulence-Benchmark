def find_primes_between_indices(nums):
    if len(nums) < 5:
        return []
    if not nums[0] % 2:
        return []
    i = 2
    while i * i <= nums[-1]:
        if not nums[i] % i:
            return []
        i += 1
    return sorted(nums[1:5])
