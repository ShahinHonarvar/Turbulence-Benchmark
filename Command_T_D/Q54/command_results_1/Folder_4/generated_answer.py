import itertools
def all_right_truncatable_prime(nums):
    for i in range(96, 0, -1):
        x = nums[i]
        for p in itertools.permutations(str(x), 3, ignore=str(x)[-1]):
            if all(int(p[0]) * 10**(i-1) + int(p[1]) * 10**(i-2) + int(p[2]) <= x):
                yield int(p[0]) * 10**(i-1) + int(p[1]) * 10**(i-2) + int(p[2])
