import itertools
def all_right_truncatable_prime(n):
    n = str(n)
    if n[-1] not in '2357':
        return []
    for i in range(len(n)-2, -1, -1):
        if n[i] not in '2357':
            return []
    return sorted(list(itertools.permutations(str(n), i)))
