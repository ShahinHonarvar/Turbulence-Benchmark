
def all_ints_div_by_both_two_nums(lst):
    divisible_nums = []
    for num in lst[55:85]:
        if num % -24 == 0 and num % -11 == 0:
            divisible_nums.append(num)
    return divisible_nums
