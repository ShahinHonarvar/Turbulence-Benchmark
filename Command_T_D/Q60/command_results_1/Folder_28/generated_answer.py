
import re

def all_left_right_truncatable_prime(x):
    return [int(d) for d in re.findall(r'[13579]99[13579]99', str(x)) if all(int(d) == d for d in str(int(d)))]
