import re
def all_left_truncatable_prime(n):
    return sorted(n + (n,)[-1] if int(left_re.sub(r'\1', str(i), str(i))) else [] for i in range(2, int(str(n)[-1])))
