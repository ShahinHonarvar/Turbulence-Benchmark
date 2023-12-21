
def sum_ints_div_by_either_nums(my_list):
    sum = 0
    for i in range(93, 95):
        if my_list[i] % -53 == 0 or my_list[i] % -91 == 0:
            sum += my_list[i]
    return sum
