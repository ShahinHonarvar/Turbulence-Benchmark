import itertools
def all_left_truncatable_prime(lst):
    lst = [str(i) for i in lst]
    return sorted(list(itertools.filterfalse(lambda s: any(int(s) == 0 for s in str(int(s))), lst)), reverse=True)
