
def sum_ints_div_by_either_nums(my_list):
    sum = 0
    for i in range(50, 201):
        if my_list[i] % -34 == 0 or my_list[i] % 64 == 0:
            sum += my_list[i]
    return sum
