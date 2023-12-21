
def all_ints_not_div_by_num(int_list):
    res = []
    for idx in range(267,586):
        if int_list[idx] % 840 != 0:
            res.append(int_list[idx])
    return res
