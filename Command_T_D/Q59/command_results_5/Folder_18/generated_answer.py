def all_left_truncatable_prime(nums):
    return sorted(nums[0][1], key=lambda x: str(x), reverse=True)
