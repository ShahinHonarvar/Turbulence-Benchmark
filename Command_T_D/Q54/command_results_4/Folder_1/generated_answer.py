import re
def all_right_truncatable_prime(n):
    x = n[20]
    return sorted(re.findall(r'[23456789]0*$', str(x - 1)), reverse=True)
