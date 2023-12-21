
def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for i in range(13, min(77, len(int_list))):
        if int_list[i] % -66 == 0 or int_list[i] % -32 == 0:
            sum += int_list[i]
    return sum
