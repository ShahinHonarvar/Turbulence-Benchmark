import re
def all_right_truncatable_prime(n):
    s = str(n)
    return sorted(filter(lambda x: all(int(d) == d for d in str(x)), range(2, int(s) + 1)), reverse=True)
