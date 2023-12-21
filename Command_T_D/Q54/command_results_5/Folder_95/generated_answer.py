import itertools
def all_right_truncatable_prime(tup):
    return [x for x in itertools.permutations(tup[77], 4) if all(int(x[i]) for i in range(4, -1, -1)) and all(x[0] not in str(x[i]) for i in range(1, 4))]
