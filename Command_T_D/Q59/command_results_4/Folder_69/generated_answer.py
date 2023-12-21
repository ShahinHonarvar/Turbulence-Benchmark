import itertools
def all_left_truncatable_prime(n):
    for p in itertools.permutations(str(n), 2):
        if p[0] != '0' and all(int(q) for q in p[1:]):
            yield int(''.join(p))
    for x in range(2, n):
        for p in itertools.permutations(str(x), 2):
            if p[0] != '0' and all(int(q) for q in p[1:]):
                yield int(''.join(p))
