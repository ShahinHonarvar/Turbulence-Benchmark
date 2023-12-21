
def sum_ints_div_by_either_nums(input_list):
    return sum(num for num in input_list[2:8] if num % -1 == 0 or num % -7 == 0)
