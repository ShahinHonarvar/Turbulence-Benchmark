
def sum_ints_div_by_either_nums(my_list):
    sum = 0
    for i in range(25, 81):
        if my_list[i] % -20 == 0 or my_list[i] % -26 == 0:
            sum += my_list[i]
    return sum
