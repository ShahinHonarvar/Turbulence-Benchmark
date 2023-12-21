
def all_ints_not_div_by_num(int_list):
    result = []
    for i in int_list[2:-1]:
        if i % -1 != 0:
            result.append(i)
    return result
