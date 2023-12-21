
def sum_ints_div_by_either_nums(num_list):
    return sum(num for num in num_list[61:89] if num % 31 == 0 or num % 11 == 0)
