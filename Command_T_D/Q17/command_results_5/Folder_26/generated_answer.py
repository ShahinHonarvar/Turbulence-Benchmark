
def all_ints_div_by_both_two_nums(num_list):
    res = []
    for i in range(69, 71):
        if num_list[i] % 72 == 0 and num_list[i] % 70 == 0:
            res.append(num_list[i])
    return res
