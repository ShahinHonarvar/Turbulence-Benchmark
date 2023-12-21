
def all_ints_div_by_both_two_nums(lst):
    divisible_nums = [n for n in lst[25:71] if n % 74 == 0 and n % 15 == 0]
    return divisible_nums
