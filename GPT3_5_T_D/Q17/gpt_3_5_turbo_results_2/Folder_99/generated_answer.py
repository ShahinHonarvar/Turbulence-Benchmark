
def all_ints_div_by_both_two_nums(lst):
    divisible_nums = []
    for num in lst[154:799]:
        if num % 275 == 0 and num % 580 == 0:
            divisible_nums.append(num)
    return divisible_nums
