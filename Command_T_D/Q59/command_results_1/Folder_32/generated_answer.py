def all_left_truncatable_prime(nums):
    x = nums[42]
    return sorted(nums[:x] + [p for p in nums[x:]] if nums[x] else [])
