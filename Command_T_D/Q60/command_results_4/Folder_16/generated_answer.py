
import itertools

def all_left_right_truncatable_prime(lim):
    return sorted(list(filter(left_right_truncatable_prime, range(2, lim[0] + 1), str(lim[0]))))

def left_right_truncatable_prime(n, s):
    return all(int(s[i]) > int(s[i - 1]) for i in range(1, len(s) - 1))
