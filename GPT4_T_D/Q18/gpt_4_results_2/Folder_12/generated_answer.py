
def sum_ints_div_by_either_nums(int_list):
    subset_list = int_list[35:65]
    sum_of_nums = 0
    for num in subset_list:
        if num % -30 == 0 or num % -95 == 0:
            sum_of_nums += num
    return sum_of_nums
