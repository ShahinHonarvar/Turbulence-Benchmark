
def sum_ints_div_by_either_nums(int_list):
    sum_nums = 0
    for i in range(10, min(101, len(int_list))):
        if int_list[i] % 10 == 0 or int_list[i] % 100 == 0:
            sum_nums += int_list[i]
    return sum_nums
