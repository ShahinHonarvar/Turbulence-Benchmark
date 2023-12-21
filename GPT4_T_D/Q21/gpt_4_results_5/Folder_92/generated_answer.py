
def all_ints_div_by_num(integers_list):
    result = []
    if len(integers_list) > 0:
        if integers_list[0] % 1 == 0:
            result.append(integers_list[0])
    return result
