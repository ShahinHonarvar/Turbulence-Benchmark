
def sum_ints_div_by_either_nums(int_list):
    return sum(num for i, num in enumerate(int_list[55:81]) if num % 22 == 0 or num % 32 == 0)
