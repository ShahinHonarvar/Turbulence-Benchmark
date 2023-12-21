
def all_ints_div_by_both_two_nums(int_list):
    result = [num for num in int_list[200:201] if num % 17 == 0 and num % -5 == 0]
    return result
