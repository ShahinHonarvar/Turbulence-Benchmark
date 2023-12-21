import itertools
def all_right_truncatable_prime(n):
    res = []
    for n_ in range(2, int(str(n)[-1]))):
        for s in itertools.permutations(str(n_)):
            if int(s[0] + '0') * 10**(len(s) - 1) == n_:
                res += [int(n_)]
    return res
