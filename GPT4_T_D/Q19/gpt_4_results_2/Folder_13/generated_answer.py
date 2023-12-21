
def all_ints_not_div_by_num(int_list):
    sublist = int_list[33:44]
    result = [num for num in sublist if num % 34 != 0]
    return result
