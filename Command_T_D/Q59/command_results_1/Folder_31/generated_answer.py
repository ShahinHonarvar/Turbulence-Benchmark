import itertools
def all_left_truncatable_prime(n):
    for l in range(2, int(str(n[50])[0] + 1)):
        p = next(x for x in itertools.permutations(str(n)[:50] + str(l)) if all(int(a) for a in str(x)))
        if p <= n and all(int(a) == 1 for a in str(p)):
            yield p
