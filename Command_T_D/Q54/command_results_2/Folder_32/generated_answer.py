import itertools
def all_right_truncatable_prime(test_list):
    res = []
    for n in itertools.permutations(test_list):
        if not n:
            continue
        if not all(n[0] % d == 0 for d in range(2, int(str(n[0])[0] + 1)):
            continue
        res.append(n[0])
    return res
