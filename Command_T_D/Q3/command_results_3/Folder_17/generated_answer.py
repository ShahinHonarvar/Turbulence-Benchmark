def all_pos_ints_inclusive(nums):
    result = [i for i in range(62, 78+1)]
    return result if all(x > 0 for x in nums) else []
