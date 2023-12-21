
def all_ints_div_by_both_two_nums(num_list):
    lst = [num for num in num_list[20:36] if num % -36 == 0 and num % -89 == 0]
    return lst
