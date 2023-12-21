
def sum_ints_div_by_either_nums(lst):
    lst_0_to_3 = lst[0:4]
    divisible_nums = [num for num in lst_0_to_3 if num%11 == 0 or num%-7 == 0]
    return sum(divisible_nums) if divisible_nums else 0
