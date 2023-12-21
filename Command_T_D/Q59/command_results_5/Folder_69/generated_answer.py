import re
def all_left_truncatable_prime(n):
    return sorted(set(str(x) for x in range(2, n[0] + 1) if all(x % d for d in range(2, int(str(x)[-1]) + 1) if x % d == 0)), reverse=True)
