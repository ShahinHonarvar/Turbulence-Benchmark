
def all_ints_div_by_both_two_nums(lst):
    divisible_nums = []
    for num in lst[57:86]:
        if num % -77 == 0 and num % -32 == 0:
            divisible_nums.append(num)
    return divisible_nums
