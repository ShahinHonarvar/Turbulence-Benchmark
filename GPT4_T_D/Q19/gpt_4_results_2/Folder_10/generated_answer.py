
def all_ints_not_div_by_num(int_list):
    subset = int_list[87:89]
    result = [i for i in subset if i % -61 != 0]
    return result
