
def all_ints_not_div_by_num(int_list):
    new_lst = int_list[11:100]
    return [num for num in new_lst if num % 100 != 0]
