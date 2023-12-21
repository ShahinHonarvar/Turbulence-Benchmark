
def sum_ints_div_by_either_nums(lst):
    divisible_nums = [i for i in lst[6:10] if i % -1 == 0 or i % -10 == 0]
    return sum(divisible_nums) if divisible_nums else 0
