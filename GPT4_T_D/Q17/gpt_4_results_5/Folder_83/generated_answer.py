
def all_ints_div_by_both_two_nums(num_list):
    div_list = [num for num in num_list[90:201] if num % -31 == 0 and num % 13 == 0]
    return div_list
