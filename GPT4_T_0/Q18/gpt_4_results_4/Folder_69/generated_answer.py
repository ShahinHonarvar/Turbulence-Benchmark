
def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for i in range(61, 89):
        if i < len(int_list) and (int_list[i] % 31 == 0 or int_list[i] % 11 == 0):
            sum += int_list[i]
    return sum
