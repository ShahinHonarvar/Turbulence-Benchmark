
def all_ints_not_div_by_num(int_lst):
    result = []
    for i in range(388, 516):
        if int_lst[i] % 310 != 0:
            result.append(int_lst[i])
    return result
