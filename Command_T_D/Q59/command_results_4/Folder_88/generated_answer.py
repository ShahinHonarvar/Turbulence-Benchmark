import itertools
def all_left_truncatable_prime(n):
    for p in sorted(n):
        yield from [q for q in range(p, n[0] + 1) if q == int(str(q)[-1]) and all(int(d) for d in str(q))]
    for p in itertools.permutations(str(n[0])):
        yield int(p)
