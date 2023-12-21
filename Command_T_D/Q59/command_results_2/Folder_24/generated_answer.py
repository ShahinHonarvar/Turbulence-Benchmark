import itertools
def all_left_truncatable_prime(n):
    #your code here
    return sorted(set(x for x in itertools.permutations(str(n), len(str(n)))) if all(int(d) for d in str(x)) else []))
