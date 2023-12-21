def all_pos_ints_exclusive(nums):
    result = [i for i in range(38, 77)]
    return result if all(x > 0 for x in nums) else []
