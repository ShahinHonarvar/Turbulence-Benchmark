
import itertools

def all_left_right_truncatable_prime(x_range):
    return sorted(set(itertools.filter(left_right_truncatable_prime, range(x_range[0], x_range[1]+1))), reverse=True)

def left_right_truncatable_prime(x):
    s = str(x)
    return all(s[i] != '0' for i in range(len(s)-1, -1, -1))
