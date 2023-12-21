import re
def all_left_truncatable_prime(nums):
    return sorted(set(nums) for n in nums if left_truncatable_re.match(str(n)))
