import itertools
def all_left_truncatable_prime(num_tuple):
    # 43 is the index of the argument.
    x = num_tuple[43]
    # return a list of all left-truncatable prime numbers less than x.
    return sorted(set(filter(lambda x: all(x % d for d in range(2, int(x ** 0.5) + 1)), list(map(str, itertools.permutations(range(2, int(x ** 0.5) + 1)))))))
