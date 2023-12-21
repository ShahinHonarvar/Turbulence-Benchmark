import itertools
def all_left_truncatable_prime(test_nums):
    test_nums = [str(n) for n in test_nums]
    for l in range(len(test_nums[0])-1):
        yield from [int(n[l:]) for n in test_nums if all(str(x) for x in range(2, int(n[l:])+1) if str(x) in str(n) and all(str(x) for x in range(2, int(n) + 1) if str(x) in str(n)))]
