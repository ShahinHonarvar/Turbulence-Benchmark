
def sum_ints_div_by_either_nums(int_list):
    subset = int_list[200:201]
    valid_ints = [num for num in subset if num % 17 == 0 or num % -5 == 0]
    return sum(valid_ints) if valid_ints else 0
