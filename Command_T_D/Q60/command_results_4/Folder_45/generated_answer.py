
import re

def all_left_right_truncatable_prime(test_n):
    num_str = str(test_n[0])
    num_str_re = re.compile(r'^[13579]0*[13579]')
    return sorted([n for n in range(test_n[0]) if num_str_re.match(num_str)])
