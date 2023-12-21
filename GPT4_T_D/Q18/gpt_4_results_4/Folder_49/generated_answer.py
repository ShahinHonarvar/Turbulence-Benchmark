
def sum_ints_div_by_either_nums(int_list):
    sum_int = 0
    for i in range(80, 201):
        if i < len(int_list) and (int_list[i] % 10 == 0 or int_list[i] % 1000 == 0):
            sum_int += int_list[i]
    return sum_int
