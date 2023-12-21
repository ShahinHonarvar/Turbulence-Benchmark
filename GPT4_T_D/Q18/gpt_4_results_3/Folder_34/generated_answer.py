
def sum_ints_div_by_either_nums(int_list):
    return sum(num for index, num in enumerate(int_list[60:201]) if num % 9 == 0 or num % 11 == 0)
