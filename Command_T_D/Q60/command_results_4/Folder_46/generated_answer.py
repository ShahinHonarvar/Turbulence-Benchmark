
import re

def all_left_right_truncatable_prime(n):
    num_str = str(n)
    left_right_str = f'{num_str[0]}{num_str[-1]}'
    return [i for i in range(2, int(num_str) + 1) if re.match(left_right_str, str(i))]
