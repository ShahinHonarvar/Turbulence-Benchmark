import re
def all_left_truncatable_prime(nums):
    num = int(nums[55])
    return sorted(set(list(re.findall(r'[1-9][0-9]0?[1-9][0-9]0?[1-9][0-9]0?[1-9][0-9]0?', str(num)))))
