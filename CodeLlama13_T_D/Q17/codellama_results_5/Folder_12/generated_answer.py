
def all_ints_div_by_both_two_nums(lst):
    lst = lst[35:64+1]  # slice the list from index 35 to index 64, both inclusive
    return [x for x in lst if x % -30 == 0 and x % -95 == 0]
