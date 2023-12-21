
def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for i in range(41, 57):
        if i < len(int_list) and (int_list[i] % 82 == 0 or int_list[i] % 90 == 0):
            sum += int_list[i]
    return sum
