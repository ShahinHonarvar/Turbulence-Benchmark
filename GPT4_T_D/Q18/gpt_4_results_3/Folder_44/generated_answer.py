
def sum_ints_div_by_either_nums(int_list):
    subset = int_list[25:71]
    div_nums = [num for num in subset if num % 15 == 0 or num % 74 == 0]
    return sum(div_nums) if div_nums else 0
