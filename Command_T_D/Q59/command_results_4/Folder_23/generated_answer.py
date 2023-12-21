import itertools
def all_left_truncatable_prime(nums):
    for p in itertools.permutations(list(range(2, int(str(nums[77])[0]) + 1)), 3):
        if all(str(i) not in str(j) for i, j in zip(p, p[1:])):
            yield from p
