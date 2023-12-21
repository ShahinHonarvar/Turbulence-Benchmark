
def sum_ints_div_by_either_nums(my_list):
    sum = 0
    for i in range(55, 84+1):
        if my_list[i] % -24 == 0 or my_list[i] % -11 == 0:
            sum += my_list[i]
    return sum
