
def sum_ints_div_by_either_nums(int_list):
    relevant_list = int_list[44:60]
    sum_divisible = sum(num for num in relevant_list if num % 39 == 0 or num % 15 == 0)
    return sum_divisible
