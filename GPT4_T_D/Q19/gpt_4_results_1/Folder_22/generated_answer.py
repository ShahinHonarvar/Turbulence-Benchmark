
def all_ints_not_div_by_num(integer_list):
    result = [x for x in integer_list[41:200] if x % 71 != 0]
    return result
