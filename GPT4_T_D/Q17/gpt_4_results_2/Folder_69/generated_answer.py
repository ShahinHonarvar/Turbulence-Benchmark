
def all_ints_div_by_both_two_nums(lst):
    sublist = lst[61:89]
    result = [num for num in sublist if num % 31 == 0 and num % 11 == 0]
    return result 
