import itertools
def all_right_truncatable_prime(tup):
    return sorted(filter(lambda x: all(int(x) % 10 ** i == 0 for i in range(1, len(str(x)))), map(lambda x: x * 10 ** i for i in range(1, len(str(x)))))
