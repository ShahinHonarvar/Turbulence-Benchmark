import itertools
def all_right_truncatable_prime(n):
    for p in itertools.permutations(str(n)):
        if all(int(d) for d in p):
            yield int(''.join(p))
    return []
