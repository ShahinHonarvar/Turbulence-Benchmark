
def sum_ints_div_by_either_nums(int_list):
    sum_ints = 0
    for i in range(90, 98, 1):
        try:
            if int_list[i] % 13 == 0 or int_list[i] % 35 == 0:
                sum_ints += int_list[i]
        except IndexError:
            break
    return sum_ints
