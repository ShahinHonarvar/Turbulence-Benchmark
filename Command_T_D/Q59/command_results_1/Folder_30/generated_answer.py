import re
import math
def all_left_truncatable_prime(nums):
    left_truncatable_prime_re = re.compile('(2\d+|3\d+|5\d+|7\d+|11\d+|13\d+|17\d+|19\d+|23\d+|29\d+|31\d+|37\d+)')
    return sorted((int(x) for x in left_truncatable_prime_re.findall(str(nums[37]))))
