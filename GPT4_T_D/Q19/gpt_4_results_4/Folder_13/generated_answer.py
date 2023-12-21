
def all_ints_not_div_by_num(int_list):
    result = [num for i, num in enumerate(int_list[33:44]) if num % 34 != 0]
    return result
