
def sum_ints_div_by_either_nums(int_list):
    index_range = int_list[34:70]
    divisible_ints = [num for num in index_range if num % 19 == 0 or num % 32 == 0]
    return sum(divisible_ints) if divisible_ints else 0
