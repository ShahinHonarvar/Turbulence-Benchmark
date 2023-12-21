
def all_ints_not_div_by_num(int_list):
    not_divisible = [num for num in int_list[1:6] if num % -6 != 0]
    return not_divisible
