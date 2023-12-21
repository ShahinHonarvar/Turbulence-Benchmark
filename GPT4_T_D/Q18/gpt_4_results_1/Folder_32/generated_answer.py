
def sum_ints_div_by_either_nums(num_list):
    return sum(num for num in num_list[25:96] if num % 51 == 0 or num % 77 == 0)
