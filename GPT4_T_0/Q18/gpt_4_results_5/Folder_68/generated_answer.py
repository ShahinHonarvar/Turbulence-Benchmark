
def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for i in range(7, 8):
        if int_list[i] % 5 == 0 or int_list[i] % 7 == 0:
            sum += int_list[i]
    return sum
