import itertools
def all_right_truncatable_prime(test_tup):
    res = list(map(str, itertools.permutations(str(test_tup[18]))))
    return sorted(list(filter(lambda x: all(int(a) == 9 for a in str(x)), res)), reverse=True)
