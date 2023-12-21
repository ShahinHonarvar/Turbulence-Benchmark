
def sum_ints_div_by_either_nums(int_list):
    sum_values = 0
    for i in range(42, min(88, len(int_list))):
        if int_list[i] % -90 == 0 or int_list[i] % -74 == 0:
            sum_values += int_list[i]
    return sum_values
