import itertools
def all_left_truncatable_prime(n):
    return sorted(set(n) for n in itertools.permutations(str(x) for x in range(2, int(n[0]) + 1) if all(str(x) for x in range(2, int(n[0]) + 1) if str(x).rstrip('0') == str(n) and all(str(x) for x in range(2, int(n[0]) + 1) if str(x).rstrip('0') == str(n) and x == int(n))))
