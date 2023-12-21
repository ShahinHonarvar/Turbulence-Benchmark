
def all_ints_not_div_by_num(int_list):
    new_list = int_list[21:43]
    result = [i for i in new_list if i % 95 != 0]
    return result
