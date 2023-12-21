
def sum_ints_div_by_either_nums(int_list):
    sub_list = int_list[44:60]
    summation = 0
    for num in sub_list:
        if num % 39 == 0 or num % 15 == 0:
            summation += num
    return summation
