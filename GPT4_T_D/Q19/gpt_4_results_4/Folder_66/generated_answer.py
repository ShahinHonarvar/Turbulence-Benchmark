
def all_ints_not_div_by_num(int_list):
    result = []
    for i in int_list[85:86]:
        if i % 99 != 0:
            result.append(i)
    return result
