
def all_ints_div_by_both_two_nums(num_list):
    result = [num for num in num_list[0:4] if num % 11 == 0 and num % -7 == 0]
    return result
