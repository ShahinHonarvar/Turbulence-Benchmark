
def sum_ints_div_by_either_nums(int_list):
    sum_divisible = 0
    for num in int_list[11:77]:
        if num % -81 == 0 or num % -94 == 0:
            sum_divisible += num
    return sum_divisible
