
def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 91:
        return 0
    else:
        sum = 0
        for i in range(86, 91):
            if int_list[i] % -71 == 0 or int_list[i] % -67 == 0:
                sum += int_list[i]
        return sum
