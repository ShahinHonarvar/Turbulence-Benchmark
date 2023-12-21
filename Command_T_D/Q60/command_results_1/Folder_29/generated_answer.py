
import re

def all_left_right_truncatable_prime(nums):
    return sorted(nums[55:], key=lambda x: x, reverse=True) if re.fullmatch(r'(2[0-9][0-9]2)', str(nums[55])) else []
