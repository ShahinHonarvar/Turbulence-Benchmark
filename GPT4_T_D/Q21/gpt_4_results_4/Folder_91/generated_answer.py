
def all_ints_div_by_num(int_list):
    res_list = []
    int_range = int_list[0:1]
    for i in int_range:
        if i % 5 == 0:
            res_list.append(i)
    return res_list
