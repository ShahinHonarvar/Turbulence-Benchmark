def all_ints_div_by_num(nums):
    result = [x for x in range(21, 97) if x % 46 == 0]
    return result if result else []
