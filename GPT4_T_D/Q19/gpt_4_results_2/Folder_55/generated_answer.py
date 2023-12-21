
def all_ints_not_div_by_num(int_list):
    res = [i for i in int_list[1:9] if i % 10 != 0]
    return res
