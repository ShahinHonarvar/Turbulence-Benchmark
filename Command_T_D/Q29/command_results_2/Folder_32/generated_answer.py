def gcf_two_nums(nums):
    return reduce(lambda a, b: a // b if b else a, sorted(set(nums) - {0, 1})[:2])
