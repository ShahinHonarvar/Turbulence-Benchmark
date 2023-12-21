def all_pos_ints_exclusive(nums):
    result = [i for i in range(70, 98)]
    return result if result & set(nums) else []
