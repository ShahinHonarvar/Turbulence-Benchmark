
import re

def all_left_right_truncatable_prime(test_list):
    return sorted(set(str(x) for x in test_list if re.fullmatch(r'[1-9][0-9]*', str(x))), reverse=True)
