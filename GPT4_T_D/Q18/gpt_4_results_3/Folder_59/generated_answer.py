
def sum_ints_div_by_either_nums(num_list):
    return sum([num for num in num_list[:9] if num % -3 == 0 or num % 8 == 0])
