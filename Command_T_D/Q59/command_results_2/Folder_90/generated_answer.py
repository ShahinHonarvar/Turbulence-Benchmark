import itertools
def all_left_truncatable_prime(x):
    return sorted(list(filter(left_truncatable_prime, range(2, x)))))
def left_truncatable_prime(n):
    s = str(n)
    for i in range(len(s)):
        if s[:i] in '2357':
            continue
        else:
            return False
    return True
