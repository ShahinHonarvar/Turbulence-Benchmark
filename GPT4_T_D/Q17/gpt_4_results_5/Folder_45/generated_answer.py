
def all_ints_div_by_both_two_nums(input_list):
    division_check = lambda x: x % -115 == 0 and x % 115 == 0
    result = [num for num in input_list[30:201] if division_check(num)]
    return result
