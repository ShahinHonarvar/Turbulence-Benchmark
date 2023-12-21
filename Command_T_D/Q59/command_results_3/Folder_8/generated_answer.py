import itertools
def all_left_truncatable_prime(test_tup):
    return sorted(list(itertools.filter(lambda x: all(str(x)[0:i] in str(y) for i in range(1, len(str(x)))), test_tup[41])), reverse=True)
