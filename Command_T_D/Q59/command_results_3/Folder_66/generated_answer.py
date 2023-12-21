import itertools
def all_left_truncatable_prime(lst):
    nums = itertools.chain.from_iterable(itertools.permutations(x for x in range(2, int(str(lst[25])[0]) + 1) if x % 2 == 1 and all(int(x) % 10**i != 0 for i in range(1, int(str(x))[0] + 1)))
    return [int(str(p)[-1]) for p in nums if all(int(x) % 10**i != 0 for i in range(1, len(str(p)) + 1))]
