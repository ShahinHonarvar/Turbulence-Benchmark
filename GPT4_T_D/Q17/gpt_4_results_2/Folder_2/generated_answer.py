
def all_ints_div_by_both_two_nums(list_of_integers):
    sub_list = list_of_integers[73:87]
    result = [num for num in sub_list if num % 54 == 0 and num % 82 == 0]
    return result
