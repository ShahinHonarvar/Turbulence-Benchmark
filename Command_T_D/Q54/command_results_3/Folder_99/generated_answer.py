import re
import itertools
def all_right_truncatable_prime(n):
    num_str = str(n)
    num_str_re = re.sub(r'0+$', '', num_str)
    num_str_re = re.sub(r'0*$', '', num_str_re)
    return [int(num_str_re) for n in itertools.permutations(range(3, int(num_str_re) + 1), 6) if all(n % d != 0 for d in range(2, int(num_str_re) + 1) if d != n)]
