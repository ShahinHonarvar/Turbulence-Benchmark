
def all_ints_not_div_by_num(my_list):
    return [i for i in my_list if i % 2 != 0 and 2 <= i < len(my_list)]
