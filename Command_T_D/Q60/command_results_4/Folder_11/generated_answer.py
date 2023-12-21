
import re
def all_left_right_truncatable_prime(n):
    s=str(n)
    if re.match(r'^[2-9][0-9][0-9]*[0-9][0-9]$', s):
        return [int(s)]
    else:
        return []
