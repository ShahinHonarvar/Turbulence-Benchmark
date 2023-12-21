
def all_ints_not_div_by_num(integer_list):
    modified_list = [i for i in integer_list[21:200] if i % -200 != 0]
    return modified_list
