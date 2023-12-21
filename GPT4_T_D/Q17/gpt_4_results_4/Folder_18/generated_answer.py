
def all_ints_div_by_both_two_nums(int_list):
    div_nums = []
    for i in range(55, 67):
        if (int_list[i] % 22 == 0) and (int_list[i] % 82 == 0):
            div_nums.append(int_list[i])
    return div_nums
