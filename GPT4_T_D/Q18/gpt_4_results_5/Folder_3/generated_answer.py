
def sum_ints_div_by_either_nums(int_list):
    valid_nums = int_list[38:53]
    total = sum(num for num in valid_nums if num % -41 == 0 or num % -47 == 0)
    return total
