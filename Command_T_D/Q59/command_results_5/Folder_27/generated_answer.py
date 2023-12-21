import itertools
import re
def all_left_truncatable_prime(tup):
    x, = tup
    x_str = str(x)
    return sorted(set(itertools.filter(lambda p: all(int(d) for d in str(p) if d!='0' and str(p)[0]=='0' and int(p) in primes)), key=lambda p: int(re.sub(r'0+$', '', str(p)))))
