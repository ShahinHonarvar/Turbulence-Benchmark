import itertools
def all_right_truncatable_prime(n):
    for i in range(1, int(str(n)[-1]) + 1):
        for p in itertools.permutations(str(n)[-1::-1]):
            if int(p[-1]) > i:
                continue
            if p[0] == '2' and p[1] == '5':
                continue
            if all(int(p[i]) > i for i in range(2, len(p))):
                yield int(p[:-1])
                break
    else:
        return []
