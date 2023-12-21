
def all_ints_not_div_by_num(int_list):
    result = []
    for index in range(25, 76):
        if int_list[index] % -53 != 0:
            result.append(int_list[index])
    return result
