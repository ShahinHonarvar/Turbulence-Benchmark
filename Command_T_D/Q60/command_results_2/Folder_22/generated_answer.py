
import re

left_re = re.compile(r'(?=0)0')
right_re = re.compile(r'(?<=9)0')

def all_left_right_truncatable_prime(nums):
    return sorted(list(filter(lambda x: left_re.sub(r'\1', str(x), x) in right_re.sub(r'\1', str(x), x), nums)))
