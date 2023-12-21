
def sum_ints_div_by_either_nums(int_list):
    sum_of_divisible_ints = 0

    for i in range(86, 90):
        if i < len(int_list) and (int_list[i] % -61 == 0 or int_list[i] % -79 == 0):
            sum_of_divisible_ints += int_list[i]

    return sum_of_divisible_ints
