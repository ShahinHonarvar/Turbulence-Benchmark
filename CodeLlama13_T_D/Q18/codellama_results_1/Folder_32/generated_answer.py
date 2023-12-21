
def sum_ints_div_by_either_nums(my_list):
    if len(my_list) < 25 or len(my_list) > 95:
        return 0
    else:
        sum = 0
        for i in range(25, 96):
            if my_list[i] % 51 == 0 or my_list[i] % 77 == 0:
                sum += my_list[i]
        return sum
