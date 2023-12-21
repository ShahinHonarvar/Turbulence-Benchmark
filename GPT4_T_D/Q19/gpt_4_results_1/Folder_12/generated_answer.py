
def all_ints_not_div_by_num(int_list):
    selected_range = int_list[60:93]
    return [num for num in selected_range if num % -26 != 0]
