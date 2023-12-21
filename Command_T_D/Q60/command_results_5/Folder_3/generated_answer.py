
import re

def all_left_right_truncatable_prime(x):
    def is_left_right_truncatable(p):
        return bool(re.match('(.*[1-9][0-9]*)[1-9][0-9][0-9][0-9]*$', str(p)))
    return sorted(x for x in range(2, x+1) if all(x%d for d in range(3, int(str(x).count('0'))+1)) and all(is_left_right_truncatable(x) for x in range(3, int(str(x).count('0'))+1)))
