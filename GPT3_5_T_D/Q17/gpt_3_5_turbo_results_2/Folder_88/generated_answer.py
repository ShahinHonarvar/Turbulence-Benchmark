
def all_ints_div_by_both_two_nums(lst):
    divisible_nums = []
    for num in lst[3:10]:
        if num % 6 == 0 and num % 1 == 0:
            divisible_nums.append(num)
    return divisible_nums
