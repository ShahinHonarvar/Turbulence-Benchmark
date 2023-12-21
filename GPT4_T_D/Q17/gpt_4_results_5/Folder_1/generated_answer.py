
def all_ints_div_by_both_two_nums(lst):
    divisible_nums = [num for num in lst[10:29] if num % -61 == 0 and num % -64 == 0]
    return divisible_nums
