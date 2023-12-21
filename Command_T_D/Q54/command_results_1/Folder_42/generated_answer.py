import itertools
def all_right_truncatable_prime(n):
    return sorted(set(itertools.permutations(str(n))).difference(
        (p for p in range(2, int(0) + 1) if all(int(d) for d in str(p)))),
        reverse=True)
