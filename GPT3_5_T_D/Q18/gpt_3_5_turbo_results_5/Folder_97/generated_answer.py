
def sum_ints_div_by_either_nums(lst):
    nums = lst[58:76]
    divisible_nums = [num for num in nums if num % 72 == 0 or num % 62 == 0]
    if divisible_nums:
        return sum(divisible_nums)
    else:
        return 0
