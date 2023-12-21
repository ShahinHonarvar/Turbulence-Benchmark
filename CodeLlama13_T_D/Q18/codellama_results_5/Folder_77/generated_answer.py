
def sum_ints_div_by_either_nums(my_list):
    start, end = 828, 932
    divisible_sum = 0
    for i in range(start, end+1):
        if my_list[i] % -649 == 0 or my_list[i] % -461 == 0:
            divisible_sum += my_list[i]
    return divisible_sum
