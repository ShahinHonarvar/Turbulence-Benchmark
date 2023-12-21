import itertools
def all_right_truncatable_prime(n):
    for p in itertools.permutations(str(n)):
        if n - int(p) > 1:
            yield int(p)
