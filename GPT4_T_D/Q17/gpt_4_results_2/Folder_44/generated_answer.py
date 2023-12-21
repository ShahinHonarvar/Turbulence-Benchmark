
def all_ints_div_by_both_two_nums(lst):
    valid_values = [i for i in lst[25:71] if i % 74 == 0 and i % 15 == 0]
    return valid_values   
