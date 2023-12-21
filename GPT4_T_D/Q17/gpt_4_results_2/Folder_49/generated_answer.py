
def all_ints_div_by_both_two_nums(int_list):
    res = []
    for i in range(80, min(201, len(int_list))):
        if int_list[i] % 10 == 0 and int_list[i] % 1000 == 0:
            res.append(int_list[i])
    return res
