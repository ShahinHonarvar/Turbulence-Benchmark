
def all_ints_not_div_by_num(int_list):
    sublist = int_list[470:566]
    result = [num for num in sublist if num % -692 != 0]
    return result
