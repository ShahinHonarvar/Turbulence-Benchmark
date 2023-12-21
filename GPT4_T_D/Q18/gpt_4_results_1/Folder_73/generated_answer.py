
def sum_ints_div_by_either_nums(lst):
    sub_list = lst[81:87]
    valid_nums = [num for num in sub_list if num % -33 == 0 or num % -62 == 0]
    return sum(valid_nums) if valid_nums else 0
