
def all_ints_not_div_by_num(int_list):
    result = []
    for i in int_list[15:21]:
        if i % -93 != 0:
            result.append(i)
    return result
