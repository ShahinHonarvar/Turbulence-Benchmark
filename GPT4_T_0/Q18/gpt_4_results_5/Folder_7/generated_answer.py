
def sum_ints_div_by_either_nums(int_list):
    sum_divisible = 0
    for i in range(543, 585):
        if i < len(int_list) and (int_list[i] % -553 == 0 or int_list[i] % -737 == 0):
            sum_divisible += int_list[i]
    return sum_divisible
