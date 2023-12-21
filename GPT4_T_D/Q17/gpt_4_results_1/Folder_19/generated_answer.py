
def all_ints_div_by_both_two_nums(lst):
    divisible_nums = [i for i in lst[1:5] if i % 4 == 0 and i % -6 == 0]
    return divisible_nums
