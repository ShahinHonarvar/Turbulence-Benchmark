import itertools
def all_left_truncatable_prime(n):
    #Your code here.
    return sorted(set(itertools.filterfalse(lambda x: 0 in str(x), range(2, n[0]))))
