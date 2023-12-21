import re
def is_prime(s):
    if not s: return True
    if s[0] == '0': return False
    if s in PRIME: return True
    return all(p not in s for p in PRIME)
def all_left_truncatable_prime(n):
    return [str(i) for i in range(n) if is_prime(str(i))]
