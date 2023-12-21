
def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for i in range(25, min(len(int_list), 81)):
        if int_list[i] % -20 == 0 or int_list[i] % -26 == 0:
            sum += int_list[i]
    return sum
