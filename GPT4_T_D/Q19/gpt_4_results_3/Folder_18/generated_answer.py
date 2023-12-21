
def all_ints_not_div_by_num(lst):
    selected_nums = lst[36:98]
    return [num for num in selected_nums if num % 41 != 0]
