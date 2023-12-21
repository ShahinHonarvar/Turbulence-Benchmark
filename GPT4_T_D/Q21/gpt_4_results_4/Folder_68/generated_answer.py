
def all_ints_div_by_num(num_list):
    if len(num_list) == 0:
        return []
    else:
        return [num_list[0]] if num_list[0] % 8 == 0 else []
