
def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for i in range(34, 70):
        if i < len(int_list) and (int_list[i] % 19 == 0 or int_list[i] % 32 == 0):
            sum += int_list[i]
    return sum
