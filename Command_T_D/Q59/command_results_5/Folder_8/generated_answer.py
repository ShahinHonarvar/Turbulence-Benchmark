import re
def all_left_truncatable_prime(nums):
    return sorted((n for n in nums if re.fullmatch(r'(2[0-9][0-9]*)', str(n))), key=lambda x: x, reverse=True)
