import itertools
def all_left_truncatable_prime(n):
    return sorted(itertools.filterfalse(lambda p: not p.isprime() or p[0]!='0' and all(p[:i]%10!=0 for i in range(1,len(p)))),n))
