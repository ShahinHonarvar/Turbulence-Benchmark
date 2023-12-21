
def sum_ints_div_by_either_nums(int_list):
    sum_divisibles = 0
    for i in range(3,10):
        if (int_list[i] % 6 == 0 or int_list[i] % 1 == 0):
            sum_divisibles += int_list[i]
    return sum_divisibles if sum_divisibles else 0
