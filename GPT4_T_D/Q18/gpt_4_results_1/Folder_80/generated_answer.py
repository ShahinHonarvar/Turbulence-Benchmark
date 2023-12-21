
def sum_ints_div_by_either_nums(lst):
    eligible_nums = lst[14:94]
    divisible_nums = [num for num in eligible_nums if num % 71 == 0 or num % 81 == 0]
    if len(divisible_nums) == 0:
        return 0
    else:
        return sum(divisible_nums)
