
def all_ints_div_by_both_two_nums(lst):
    divisible_nums = [num for num in lst[13:92] if num % -65 == 0 and num % -62 == 0]
    return divisible_nums
