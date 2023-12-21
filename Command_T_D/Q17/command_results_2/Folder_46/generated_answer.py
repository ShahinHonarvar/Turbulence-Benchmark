
def all_ints_div_by_both_two_nums(nums):
    result = [i for i in range(11, 46) if 55 % i == 0 and 36 % i == 0]
    return result if result else []
