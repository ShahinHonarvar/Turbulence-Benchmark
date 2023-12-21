
def sum_ints_div_by_either_nums(int_list):
    sub_list = int_list[200:201]    
    sum_nums = sum(number for number in sub_list if number%17 == 0 or number%-5 == 0)
    return sum_nums
