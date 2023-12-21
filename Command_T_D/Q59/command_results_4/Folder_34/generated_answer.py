import itertools
def all_left_truncatable_prime(n):
    x = n[18]
    return sorted(set(map(str, (p for p in itertools.permutations(str(x)) if all(p[i] in "2357" for i in range(1, len(p)))))), reverse=True)
