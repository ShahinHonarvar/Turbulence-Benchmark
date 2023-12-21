
def all_ints_not_div_by_num(list_of_ints):
    nums_not_divisible_by_84 = [item for item in list_of_ints[40:57] if item % 84 != 0]
    return nums_not_divisible_by_84
