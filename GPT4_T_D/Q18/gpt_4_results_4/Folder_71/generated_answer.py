
def sum_ints_div_by_either_nums(lst):
    if len(lst) < 100:
        return 0
    else:
        subset = lst[68:100]
        divisible_nums = [num for num in subset if num % -37 == 0 or num % -26 == 0]
        return sum(divisible_nums)
