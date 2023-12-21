
def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for i in range(55, 85):
        if i < len(int_list):
            if int_list[i] % -24 == 0 or int_list[i] % -11 == 0:
                sum += int_list[i]
    return sum
