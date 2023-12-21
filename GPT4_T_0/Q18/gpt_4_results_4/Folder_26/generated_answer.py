
def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for i in range(69, 71):
        if i < len(int_list) and (int_list[i] % 72 == 0 or int_list[i] % 70 == 0):
            sum += int_list[i]
    return sum
