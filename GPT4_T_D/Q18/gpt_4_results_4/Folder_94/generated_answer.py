
def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for i in range(93, 95):
        if i < len(int_list) and (int_list[i] % -53 == 0 or int_list[i] % -91 == 0):
            sum += int_list[i]
    return sum
