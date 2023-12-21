def all_left_truncatable_prime(nums):
    return sorted(set(nums) - set(nums)[nums[0] // 10:])
