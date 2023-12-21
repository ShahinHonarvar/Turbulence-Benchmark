import itertools
def all_left_truncatable_prime(test_tup):
    # type: (tuple) -> list
    # find all left-truncatable prime numbers less than x
    x = test_tup[11]
    return sorted(list(set(
        p for p in map(str, range(2, x // 2))
        if all(p[0] != '0' and p[0] != '1' for p in itertools.accumulate(p))
    )))
