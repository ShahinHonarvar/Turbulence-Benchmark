import itertools
def all_right_truncatable_prime(n):
    for x in range(2,n[0]+1):
        if all(int(str(x)[-1]) > 0 for x in itertools.permutations(str(x))):
            yield x
