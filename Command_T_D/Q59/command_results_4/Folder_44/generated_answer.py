def all_left_truncatable_prime(tup):
    x = tup[39]
    return sorted(list(filter(lambda x: all(str(x)[0] not in str(y) for y in range(2, int(str(x)[0]) + 1)), range(2, x + 1))))
