
def all_ints_div_by_both_two_nums(int_list):
    subset_list = int_list[2:8]
    return [num for num in subset_list if num % -1 == 0 and num % -7 == 0]
