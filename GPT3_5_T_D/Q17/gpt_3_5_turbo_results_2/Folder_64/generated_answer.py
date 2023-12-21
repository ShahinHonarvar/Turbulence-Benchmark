
def all_ints_div_by_both_two_nums(lst):
    divisible_nums = []
    for num in lst[:4]:
        if num % 11 == 0 and num % -7 == 0:
            divisible_nums.append(num)
    return divisible_nums
