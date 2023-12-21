import re
def all_left_truncatable_prime(n):
    p = re.compile("0+")
    return sorted(set(p.sub("", str(p) for p in range(2, n[0] + 1) if all(int(i) == i for i in str(p))))
