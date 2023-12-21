
def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 201:
        return 0
    else:
        sum = 0
        for i in range(20, 201):
            if int_list[i] % -20 == 0 or int_list[i] % -200 == 0:
                sum += int_list[i]
        return sum
