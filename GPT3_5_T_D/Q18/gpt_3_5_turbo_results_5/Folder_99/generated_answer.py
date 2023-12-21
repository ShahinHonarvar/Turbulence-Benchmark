
def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for i in range(154, 799):
        if int_list[i] % 275 == 0 or int_list[i] % 580 == 0:
            sum += int_list[i]
    return sum
