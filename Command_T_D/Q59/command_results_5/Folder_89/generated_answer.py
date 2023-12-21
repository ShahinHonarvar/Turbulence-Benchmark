def all_left_truncatable_prime(nums):
    return sorted(nums[97:], key=lambda x: str(x)[1:])
