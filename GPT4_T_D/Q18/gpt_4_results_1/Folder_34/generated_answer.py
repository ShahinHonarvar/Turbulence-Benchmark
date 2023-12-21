
def sum_ints_div_by_either_nums(int_list):
    sub_list = int_list[60:201]
    sum_ints = 0
    for num in sub_list:
        if num % 9 == 0 or num % 11 == 0:
            sum_ints += num
    return sum_ints
