
import re

left_right_re = re.compile(r'(?<=0)[0-9]')
left_right_strip = lambda x: x.lstrip('0')
left_right_is_prime = lambda x: all(x % i for i in range(2, int(x) // 2 + 1))


def all_left_right_truncatable_prime(nums):
    return sorted(set(nums) for num in nums if left_right_is_prime(left_right_strip(num)))
