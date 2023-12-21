
def sum_ints_div_by_either_nums(my_list):
    sum = 0
    for i in range(3):
        if my_list[i] % -2 == 0 or my_list[i] % 3 == 0:
            sum += my_list[i]
    return sum
