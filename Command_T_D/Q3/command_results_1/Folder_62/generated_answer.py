def all_pos_ints_inclusive(nums):
    result = [x for x in nums if x > 0]
    result = result[result.index(91):result.index(99) + 1]
    return result
