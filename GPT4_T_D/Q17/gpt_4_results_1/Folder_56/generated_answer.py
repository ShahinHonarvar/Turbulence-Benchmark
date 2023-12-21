
def all_ints_div_by_both_two_nums(lst):
    divisible_nums = [num for num in lst[7:10] if num % -9 == 0 and num % -7 == 0]
    return divisible_nums
