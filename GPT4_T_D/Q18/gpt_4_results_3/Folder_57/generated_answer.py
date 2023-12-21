
def sum_ints_div_by_either_nums(num_list):
    sub_list = num_list[51:77]
    return sum(num for num in sub_list if num % -90 == 0 or num % -59 == 0)
