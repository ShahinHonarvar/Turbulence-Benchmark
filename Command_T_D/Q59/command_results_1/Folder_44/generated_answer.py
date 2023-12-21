import re
def all_left_truncatable_prime(n):
    return sorted(n[i] for i in range(1, len(n)) if n[i] != 0 and re.match(r'^[2-9][0-9]*$', str(n[i])))
