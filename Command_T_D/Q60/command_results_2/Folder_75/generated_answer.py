
import re

def all_left_right_truncatable_prime(nums):
    return [str(x) for x in nums if re.fullmatch(r'(2[1-9][0-9]*)[2-9][0-9]0(1[0-9][0-9]*)', str(x)) and x > 1]
