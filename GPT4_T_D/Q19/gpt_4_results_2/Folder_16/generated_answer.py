
def all_ints_not_div_by_num(int_list):
    sublist = int_list[25:32]
    result = [num for num in sublist if num % 35 != 0]
    return result
