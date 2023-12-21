
def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for i in range(7,10):
        if int_list[i] % -9 == 0 or int_list[i] % -7 == 0:
            sum += int_list[i]
    return sum if sum != 0 else 0
