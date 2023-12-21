
def all_ints_not_div_by_num(int_list):
    result = []
    for i in int_list[1:4]:
        if i % 8 != 0:
            result.append(i)
    return result
