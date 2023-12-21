
def all_pos_ints_exclusive(nums):
    return [x for x in nums if 10 < x < 100 and isinstance(x, int)]
