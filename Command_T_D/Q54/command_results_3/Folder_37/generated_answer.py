def all_right_truncatable_prime(nums):
    return sorted(set(range(3, nums[35] // 2)), key=lambda x: str(x) + str(x // 10))
