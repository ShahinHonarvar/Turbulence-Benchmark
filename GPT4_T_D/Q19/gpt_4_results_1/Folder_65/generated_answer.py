
def all_ints_not_div_by_num(int_list):
    subset = int_list[16:51]
    result = [num for num in subset if num % -34 != 0]
    return result
