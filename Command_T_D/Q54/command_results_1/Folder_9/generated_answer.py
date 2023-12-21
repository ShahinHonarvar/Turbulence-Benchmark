import itertools
def all_right_truncatable_prime(n):
    return [x for x in sorted(set(itertools.permutations(str(n)))), key=lambda s: int(s)) if all(x%y!=0 for x,y in zip(x, range(2, int(x ** .5) + 1)))]
