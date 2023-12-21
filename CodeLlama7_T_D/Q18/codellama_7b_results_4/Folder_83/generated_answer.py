
def sum_ints_div_by_either_nums(my_list):
    sum = 0
    for i in range(90, 201):
        if my_list[i] % -31 == 0 or my_list[i] % 13 == 0:
            sum += my_list[i]
    return sum
