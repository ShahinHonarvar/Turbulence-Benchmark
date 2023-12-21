
def sum_ints_div_by_either_nums(int_list):
    sum_of_ints = 0
    for i in range(36, 86):
        if i < len(int_list):
            if int_list[i] % -27 == 0 or int_list[i] % -96 == 0:
                sum_of_ints += int_list[i]
    return sum_of_ints
