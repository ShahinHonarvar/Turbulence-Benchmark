def gcf_two_nums(nums):
    return reduce(lambda a, b: a // b if b else a, set(nums) - {0})
