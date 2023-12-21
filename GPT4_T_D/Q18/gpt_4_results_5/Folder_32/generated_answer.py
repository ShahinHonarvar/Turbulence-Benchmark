
def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 96:
        return 0
    else:
        sum = 0
        for i in range(25, 96):
            if int_list[i] % 51 == 0 or int_list[i] % 77 == 0:
                sum += int_list[i]
        return sum
