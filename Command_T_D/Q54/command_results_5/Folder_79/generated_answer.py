import itertools
def all_right_truncatable_prime(n):
    return sorted(filter(lambda x: n[x] < x, range(1, int(str(n[91])[0]))) for x in itertools.permutations(str(n[91])))
