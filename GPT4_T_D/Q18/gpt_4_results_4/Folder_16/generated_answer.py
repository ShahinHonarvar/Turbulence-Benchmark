
def sum_ints_div_by_either_nums(int_list):
    sub_list = int_list[55:81]
    sum_nums = sum(num for num in sub_list if num % 22 == 0 or num % 32 == 0)
    return sum_nums
