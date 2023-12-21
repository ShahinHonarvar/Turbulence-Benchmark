
def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for i in range(56, min(89, len(int_list))):
        if int_list[i] % -59 == 0 or int_list[i] % -79 == 0:
            sum += int_list[i]
    return sum
