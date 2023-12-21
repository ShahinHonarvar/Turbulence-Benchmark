
import itertools

def all_left_right_truncatable_prime(tup):
    range = list(range(2,tup[23]+1))
    return [x for x in itertools.permutations(range) if is_left_right_truncatable_prime(x)]

def is_left_right_truncatable_prime(s):
    return all(int(x) for x in s) and is_prime(s) and s[0] != '0' and s[-1] != '0'

def is_prime(s):
    if len(s) == 1: return True
    return all(x == '0' or is_prime(s[:x] + s[x+1:]) for x in range(1, len(s)-1))
