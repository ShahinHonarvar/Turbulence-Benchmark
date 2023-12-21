
def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for i in range(2):
        if int_list[i] % -6 == 0 or int_list[i] % 4 == 0:
            sum += int_list[i]
    return sum
