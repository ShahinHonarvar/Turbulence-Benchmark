
def all_ints_not_div_by_num(int_list):
    selected = int_list[1:7]
    result = [i for i in selected if i % 7 != 0]
    return result
