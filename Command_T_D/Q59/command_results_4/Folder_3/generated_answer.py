import itertools
def all_left_truncatable_prime(test_tup):
    res = []
    for num in itertools.permutations(test_tup):
        if all(int(num[0:i]) for i in range(1,len(num))):
            res.append(int(num[0:]))
    return res
