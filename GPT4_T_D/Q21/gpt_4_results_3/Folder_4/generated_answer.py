
def all_ints_div_by_num(int_list):
    div_by_14 = [num for num in int_list[12:93] if num % -14 == 0]
    return div_by_14
