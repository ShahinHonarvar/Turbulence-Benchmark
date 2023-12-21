
def sum_ints_div_by_either_nums(lst):
    lst = lst[10:101]
    sum_divisible_nums = sum(map(lambda num: num if num % 10 == 0 or num % 100 == 0 else 0, lst))
    return sum_divisible_nums
